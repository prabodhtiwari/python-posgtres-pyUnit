echo "USE CASE: Postgres database setup"
python postgres_setup_test.py

echo "USE CASE: Hive database setup"
python hive_test.py

echo "USE CASE: Test Pig script produces CSV"
python pig_test.py

echo "USE CASE: Import data from CSVs into Hive via spark-submit"
python import_hive_spark_submit.py

echo "USE CASE: Export data from Hive via Hive SQL file"
python export_hive_by_hive_sql.py

echo "USE CASE: Test spark-submit for the aggregations"
python spark_submit_for_aggregation.py