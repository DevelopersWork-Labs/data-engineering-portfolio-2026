import re
from pyspark.sql import functions as F

def ingest_raw_to_bronze(source_path, schema_name, table_name, mode='append'):

    source_df = spark.read.csv(source_path, header=True, inferSchema=False)

    renamed_columns = dict()
    for col in source_df.columns:
        renamed_columns[col] = re.sub(r'[^a-zA-Z0-9]', '_', col.lower())

    raw_df = (
        source_df
        .withColumn('_hash_md5', F.md5(F.concat_ws(',', *source_df.columns)))
        .withColumn('_ingest_timestamp', F.current_timestamp())
        .withColumn('_ingest_author', F.current_user())
        .withColumn('_source_file', F.col("_metadata.file_path"))
        .withColumnsRenamed(renamed_columns)
    )

    (
        raw_df
        .write
        .format('delta')
        .mode(mode)
        .option('mergeSchema', True)
        .saveAsTable(f'{schema_name}.bronze_{table_name}')
    )


if __name__ == '__main__':
    SCHEMA_NAME = 'lab_2026'
    TABLE_NAME = 'online_retail'
    ingest_raw_to_bronze(csv_file_path, SCHEMA_NAME, TABLE_NAME)
    spark.read.table(f'{SCHEMA_NAME}.bronze_{TABLE_NAME}').display()