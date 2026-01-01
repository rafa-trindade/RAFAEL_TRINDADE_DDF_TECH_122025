# 🏛️ Data Governance - Mapeamento Prático do Projeto

Este diretório concentra as **políticas, diretrizes e decisões estruturais**
relacionadas à governança de dados do projeto.

O objetivo da governança é garantir que os dados sejam:
- Confiáveis
- Reprocessáveis
- Auditáveis
- Sustentáveis em custo
- Alinhados às necessidades do negócio

A governança neste projeto é **pragmática**, orientada a engenharia e operação,
evitando complexidade desnecessária.

---

## 📌 Escopo da Governança

A governança de dados neste projeto cobre:

- Organização lógica do Data Lake
- Estratégias de retenção e descarte
- Separação clara entre camadas técnicas e semânticas
- Regras de reprocessamento
- Definição de contratos de qualidade
- Suporte à observabilidade e auditoria

---

## 📄 Documentos Disponíveis

### 🧹 Política de Retenção e Versionamento de Dados
Arquivo: [`/politica_retencao.md`](politica_retencao.md)


Define:
- Estratégia de retenção baseada em runs
- Estrutura de pastas por execução (`run_id`)
- Quantidade máxima de histórico por camada
- Momento seguro de limpeza
- Garantias de rollback e reprocessamento

---

## 🔗 Integração com Outros Domínios

A governança atua de forma integrada com:

- **Data Architecture:** define o desenho físico e lógico do lake
- **Data Lineage:** permite rastreabilidade ponta a ponta
- **Data Quality:** garante confiabilidade semântica
- **Data Observability:** monitora saúde e comportamento dos dados

Governança, neste contexto, **não é um silo**, mas uma camada transversal.

---

## 🎯 Princípios Norteadores

- Simplicidade operacional
- Transparência técnica
- Custos controlados
- Reprocessamento como regra, não exceção
- Governança aplicada via código e automação
