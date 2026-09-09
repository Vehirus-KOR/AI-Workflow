import sys
from datetime import timedelta

import pendulum
from airflow.sdk import dag, task

sys.path.append("/opt/airflow/include")

from sales_etl import clean_sales, create_summary, load_sqlite


INPUT_PATH = "/opt/airflow/data/sales.csv"
CLEANED_PATH = "/opt/airflow/output/cleaned_sales.csv"
DATABASE_PATH = "/opt/airflow/output/sales.db"
SUMMARY_PATH = "/opt/airflow/output/summary.json"


@dag(
    dag_id="daily_sales_etl",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["practice", "etl", "sales"],
    default_args={"retries": 1, "retry_delay": timedelta(seconds=10)},
)
def daily_sales_etl():
    @task
    def extract() -> str:
        """Return the source location; the path is passed through XCom."""
        return INPUT_PATH

    @task
    def transform(input_path: str) -> dict:
        return clean_sales(input_path, CLEANED_PATH)

    @task
    def load(transform_result: dict) -> dict:
        return load_sqlite(transform_result["cleaned_path"], DATABASE_PATH)

    @task
    def report(transform_result: dict, load_result: dict) -> dict:
        summary = create_summary(transform_result["cleaned_path"], SUMMARY_PATH)
        summary["accepted"] = transform_result["accepted"]
        summary["rejected"] = transform_result["rejected"]
        summary["loaded_rows"] = load_result["loaded_rows"]
        return summary

    source_path = extract()
    transformed = transform(source_path)
    loaded = load(transformed)
    report(transformed, loaded)


daily_sales_etl()
