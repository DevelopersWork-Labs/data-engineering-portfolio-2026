from pyspark.sql import functions as F, Window as W
from delta.tables import DeltaTable

SCHEMA_NAME = 'lab_2026'
SOURCE_TABLE_NAME = 'bronze_online_retail'
TARGET_TABLE_NAME = 'silver_online_retail'

def transform_to_silver():
    
    _duplicate_window = (
        W
        .partitionBy('invoice', 'stockcode')
        .orderBy(
            F.col('invoicedate').desc()
            , F.col('_ingest_timestamp').desc()
        )
    )
    online_retail_df = (
        spark.read.table(f'{SCHEMA_NAME}.{SOURCE_TABLE_NAME}')
        .selectExpr(
            "invoice", "stockcode", "CAST(CAST(customer_id AS NUMERIC) AS BIGINT) customer_id"
            , "CAST(quantity AS BIGINT) quantity", "CAST(price AS DECIMAL(10, 2)) price"
            , "CAST(invoicedate AS TIMESTAMP) invoicedate", "country", "description"
            , '_ingest_timestamp'
        )
        .withColumn('rw', F.row_number().over(_duplicate_window))
        .filter(F.col('rw') == 1)
        .drop('rw', '_ingest_timestamp')
    )

    (
        DeltaTable
        .forName(spark, f'{SCHEMA_NAME}.{TARGET_TABLE_NAME}')
        .alias('silver')
        .merge(
            online_retail_df.alias('src')
            , 'src.invoice = silver.invoice AND src.stockcode = silver.stockcode'
        )
        .whenMatchedUpdate(
            set = {
                'customer_id': 'src.customer_id'
                , 'quantity': 'src.quantity'
                , 'price': 'src.price'
                , 'invoicedate': 'src.invoicedate'
                , 'country': 'src.country'
                , 'description': 'src.description'
                , '_update_timestamp': F.current_timestamp()
            }
        )
        .whenNotMatchedInsert(
            values = {
                'invoice': 'src.invoice'
                , 'stockcode': 'src.stockcode'
                , 'customer_id': 'src.customer_id'
                , 'quantity': 'src.quantity'
                , 'price': 'src.price'
                , 'invoicedate': 'src.invoicedate'
                , 'country': 'src.country'
                , 'description': 'src.description'
                , '_insert_timestamp': F.current_timestamp()
                , '_update_timestamp': F.current_timestamp()
            }
        )
        .execute()
    )

if __name__ == '__main__':
    transform_to_silver()