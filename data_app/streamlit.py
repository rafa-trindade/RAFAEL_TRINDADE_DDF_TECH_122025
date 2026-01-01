import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_engine

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO
# -----------------------------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="RAFAEL_TRINDADE_DDF_TECH_122025", 
    initial_sidebar_state="expanded", 
    page_icon="📊")

engine = get_engine()


# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------

QUERY_ANOS = """
    SELECT DISTINCT 
        ano 
    FROM dw_marts.mart_sales_monthly 
    ORDER BY ano DESC
"""
df_anos = pd.read_sql(QUERY_ANOS, engine)
lista_anos = df_anos["ano"].dropna().astype(int).tolist()

opcoes_filtro = ["Todos"] + lista_anos

header_filter = st.container(border=True)

with header_filter:

  col1, col2 = st.columns(2)

  with col1:
     
     with st.container(border=True):
   
      ano_selecionado = st.selectbox(
          "Selecione o Ano", 
          options=opcoes_filtro,
          index=2 if len(opcoes_filtro) > 1 else 0
      )

      if ano_selecionado == "Todos":
          condicao_ano = ",".join(map(str, lista_anos))
          label_filtro = "Todos os anos"
      else:
          condicao_ano = str(ano_selecionado)
          label_filtro = f"{ano_selecionado}"


      QUERY_TOTAL = f"""
          SELECT 
              SUM(receita_mensal) AS total 
          FROM dw_marts.mart_sales_monthly 
          WHERE ano IN ({condicao_ano})
      """
      df_total = pd.read_sql(QUERY_TOTAL, engine)
      receita_total = df_total["total"].iloc[0] or 0

  with col2:

    with st.container(border=True):
        st.metric(label=f"Receita ({label_filtro})", value=f"R$ {receita_total:,.2f}")


# -----------------------------------------------------------------------------
# 📉 LINHA 1: 
# -----------------------------------------------------------------------------
linha_1 = st.container(border=True)

with linha_1:
    QUERY_CATEGORY = f"""
        SELECT 
            product_category_name,
            SUM(receita_categoria) AS receita_categoria
        FROM dw_marts.mart_product_category_performance
        WHERE ano IN ({condicao_ano})
        GROUP BY product_category_name
        ORDER BY receita_categoria DESC
        LIMIT 15
    """
    
    df_category = pd.read_sql(QUERY_CATEGORY, engine)

    fig1 = px.bar(
        df_category,
        x="receita_categoria",
        y="product_category_name",
        orientation="h",
        color="receita_categoria",
        color_continuous_scale=px.colors.sequential.Blues,
        template="plotly_white",
        title="💰 Receita por Categoria"
    )

    fig1.update_layout(
        showlegend=False,
        yaxis=dict(
            categoryorder="total ascending"
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )

    st.plotly_chart(fig1, use_container_width=True)


# -----------------------------------------------------------------------------
# 📊 LINHA 2
# -----------------------------------------------------------------------------

linha_2 = st.container(border=True)

with linha_2:
    top_n = st.slider("Quantidade de Categorias", 5, 20, 10)

    QUERY_GROWTH = f"""
        SELECT 
            product_category_name, 
            ano, 
            mes, 
            crescimento_percentual 
        FROM dw_marts.mart_category_growth_monthly 
        WHERE crescimento_percentual IS NOT NULL 
          AND ano IN ({condicao_ano})
    """
    
    df_growth = pd.read_sql(QUERY_GROWTH, engine)

    df_growth["periodo"] = (
        df_growth["ano"].astype(str) + "-" +
        df_growth["mes"].astype(str).str.zfill(2)
    )

    top_categories = (
        df_growth
        .groupby("product_category_name")["crescimento_percentual"]
        .mean()
        .nlargest(top_n)
        .index
    )

    df_growth = df_growth[df_growth["product_category_name"].isin(top_categories)]

    df_growth = (
        df_growth
        .groupby(["product_category_name", "periodo"], as_index=False)
        .agg({"crescimento_percentual": "mean"})
    )

    heatmap_data = df_growth.pivot(
        index="product_category_name",
        columns="periodo",
        values="crescimento_percentual"
    )

    heatmap_data = heatmap_data.loc[
        heatmap_data.mean(axis=1).sort_values(ascending=False).index
    ]

    fig2 = px.imshow(
        heatmap_data,
        color_continuous_scale="RdBu_r",
        aspect="auto",
        text_auto=".1f",
        template="plotly_white",
        title="📈 Crescimento Mensal (%)"
    )

    fig2.update_layout(
        coloraxis_colorbar=dict(title="%"),
        margin=dict(l=0, r=0, t=35, b=0)
    )

    st.plotly_chart(fig2, use_container_width=True)



# -----------------------------------------------------------------------------
# 📉 LINHA 3: 
# -----------------------------------------------------------------------------

linha_3 = st.container(border=True)

with linha_3:

  col3, col4 = st.columns(2)


  with col3:
      
      with st.container(border=True):
      
        QUERY_DAILY = f"""
            SELECT 
                data, 
                receita_diaria 
            FROM dw_marts.mart_sales_daily 
            WHERE EXTRACT(YEAR FROM data) IN ({condicao_ano}) 
            ORDER BY data
        """
        df_daily = pd.read_sql(QUERY_DAILY, engine)
        
        fig3 = px.line(
            df_daily,
            x="data",
            y="receita_diaria",
            template="plotly_white",
            title="📅 Receita Diária"
        )

        fig3.update_layout(
            margin=dict(l=0, r=0, t=50, b=0)
        )

        fig3.update_traces(
            line=dict(color="#005B96", width=2)
        )
        
        st.plotly_chart(fig3, use_container_width=True)


  with col4:
    with st.container(border=True):

        QUERY_WEEKDAY = """
            SELECT 
                nome_dia_semana, 
                receita_total 
            FROM dw_marts.mart_sales_weekda
        """
        df_weekday = pd.read_sql(QUERY_WEEKDAY, engine)
        ordem_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

        fig4 = px.bar(
            df_weekday,
            x="nome_dia_semana",
            y="receita_total",
            category_orders={"nome_dia_semana": ordem_semana},
            template="plotly_white",
            title="📆 Receita por Dia da Semana"
        )
    
        fig4.update_layout(
            margin=dict(l=0, r=0, t=50, b=0)
        )

        fig4.update_traces(marker_color="#005B96")
        
        st.plotly_chart(fig4, use_container_width=True)

# -----------------------------------------------------------------------------
# 📉 LINHA 4: 
# -----------------------------------------------------------------------------

linha_4 = st.container(border=True)

with linha_4:

    QUERY_MONTHLY = f"""
    SELECT 
        ano, 
        mes, 
        receita_mensal 
    FROM dw_marts.mart_sales_monthly 
    WHERE ano IN ({condicao_ano}) 
    ORDER BY ano, mes
    """
    df_monthly = pd.read_sql(QUERY_MONTHLY, engine)
    df_monthly["periodo"] = df_monthly["ano"].astype(str) + "-" + df_monthly["mes"].astype(str).str.zfill(2)

    df_monthly["data"] = pd.to_datetime(
        df_monthly["ano"].astype(str) + "-" +
        df_monthly["mes"].astype(str) + "-01"
    )

    fig5 = px.line(
        df_monthly,
        x="data",
        y="receita_mensal",
        markers=True,
        template="plotly_white",
        title="📈 Receita Mensal Total"
    )

    fig5.update_layout(
        margin=dict(l=0, r=0, t=50, b=0)
    )

    fig5.update_traces(
        line=dict(color="#004A7C", width=2)
    )


    st.plotly_chart(fig5, use_container_width=True)


