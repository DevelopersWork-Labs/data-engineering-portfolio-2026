from pyspark.sql import functions as F, types as T
from delta.tables import DeltaTable

SCHEMA_NAME = 'lab_2026'
SOURCE_TABLE_NAME = 'silver_online_retail'
TARGET_TABLE_NAME = 'gold_daily_sales'

def model_to_gold():
    
    online_retail_df = (
        spark.read.table(f'{SCHEMA_NAME}.{SOURCE_TABLE_NAME}')
        .withColumn('invoice_date', F.col('invoicedate').cast(T.DateType()))
        .groupBy('country', 'invoice_date')
        .agg(
            F.sum(F.col('price') * F.col('quantity')).alias('total_revenue')
            , F.countDistinct(F.col('invoice')).alias('total_orders')
        )
        .withColumn('_insert_timestamp', F.current_timestamp())
        .withColumn('_update_timestamp', F.current_timestamp())
    )

    (
        DeltaTable
        .forName(spark, f'{SCHEMA_NAME}.{TARGET_TABLE_NAME}')
        .alias('gold')
        .merge(
            online_retail_df.alias('src')
            , 'gold.country = src.country AND gold.invoice_date = src.invoice_date'
        )
        .whenMatchedUpdate(
            set = {
                'total_revenue': 'src.total_revenue'
                , 'total_orders': 'src.total_orders'
                , '_update_timestamp': 'src._update_timestamp'
            }
        )
        .whenNotMatchedInsertAll()
        .execute()
    )

if __name__ == '__main__':
    model_to_gold()