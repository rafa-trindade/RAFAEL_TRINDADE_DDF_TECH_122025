import pandera.pandas as pa
from pandera import Column, DataFrameSchema


customers_schema = DataFrameSchema({
    "customer_id": Column(pa.String, nullable=True),
    "customer_unique_id": Column(pa.String, nullable=True),
    "customer_zip_code_prefix": Column(pa.Int, nullable=True),
    "customer_city": Column(pa.String, nullable=True),
    "customer_state": Column(pa.String, nullable=True),
    "run_id": Column(pa.Int, nullable=True),
})


geolocation_schema = DataFrameSchema({
    "geolocation_zip_code_prefix": Column(pa.Int, nullable=True),
    "geolocation_lat": Column(pa.Float, nullable=True),
    "geolocation_lng": Column(pa.Float, nullable=True),
    "geolocation_city": Column(pa.String, nullable=True),
    "geolocation_state": Column(pa.String, nullable=True),
    "run_id": Column(pa.Int, nullable=True),
})


order_items_schema = DataFrameSchema({
    "order_id": Column(pa.String, nullable=True),
    "order_item_id": Column(pa.Int, nullable=True),
    "product_id": Column(pa.String, nullable=True),
    "seller_id": Column(pa.String, nullable=True),
    "shipping_limit_date": Column(pa.String, nullable=True),
    "price": Column(pa.Float, nullable=True),
    "freight_value": Column(pa.Float, nullable=True),
    "run_id": Column(pa.Int, nullable=True),
})


orders_schema = DataFrameSchema({
    "order_id": Column(pa.String, nullable=True),
    "customer_id": Column(pa.String, nullable=True),
    "order_status": Column(pa.String, nullable=True),
    "order_purchase_timestamp": Column(pa.String, nullable=True),
    "order_approved_at": Column(pa.String, nullable=True),
    "order_delivered_carrier_date": Column(pa.String, nullable=True),
    "order_delivered_customer_date": Column(pa.String, nullable=True),
    "order_estimated_delivery_date": Column(pa.String, nullable=True),
    "run_id": Column(pa.Int, nullable=True),
})


products_schema = DataFrameSchema({
    "product_id": Column(pa.String, nullable=True),
    "product_category_name": Column(pa.String, nullable=True),
    "product_name_lenght": Column(pa.Float, nullable=True),
    "product_description_lenght": Column(pa.Float, nullable=True),
    "product_photos_qty": Column(pa.Float, nullable=True),
    "product_weight_g": Column(pa.Float, nullable=True),
    "product_length_cm": Column(pa.Float, nullable=True),
    "product_height_cm": Column(pa.Float, nullable=True),
    "product_width_cm": Column(pa.Float, nullable=True),
    "run_id": Column(pa.Int, nullable=True),
})


LANDING_SCHEMAS = {
    "olist_customers_dataset": customers_schema,
    "olist_geolocation_dataset": geolocation_schema,
    "olist_order_items_dataset": order_items_schema,
    "olist_orders_dataset": orders_schema,
    "olist_products_dataset": products_schema,
}
