def ingest_raw_to_bronze(source_path, table_name):
    from pyspark.sql import functions as F

    source_df = spark.read.csv(source_path, header=True, inferSchema=False)

    renamed_columns = dict()
    for col in source_df.columns:
        renamed_columns[col] = col.replace(' ', '_').lower()

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
        .mode('overwrite')
        .option('mergeSchema', True)
        .saveAsTable(table_name)
    )

if __name__ == '__main__':
    table_name = f'{SCHEMA_NAME}.bronze_online_retail'
    ingest_raw_to_bronze(csv_file_path, table_name)
    spark.read.table(table_name).display()