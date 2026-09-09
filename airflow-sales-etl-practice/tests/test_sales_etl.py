import csv
import json
import sqlite3
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1] / "include"))

from sales_etl import clean_sales, create_summary, load_sqlite


def write_sample(path: Path):
    path.write_text(
        "order_id,order_date,category,quantity,unit_price,status\n"
        "A1,2026-09-01,book,2,1000,completed\n"
        "A2,2026-09-01,food,1,3000,cancelled\n"
        "A3,2026-09-01,food,0,3000,completed\n",
        encoding="utf-8",
    )


def test_etl_functions(tmp_path):
    source = tmp_path / "input.csv"
    cleaned = tmp_path / "cleaned.csv"
    database = tmp_path / "sales.db"
    summary_file = tmp_path / "summary.json"
    write_sample(source)

    result = clean_sales(str(source), str(cleaned))
    assert result["accepted"] == 1
    assert result["rejected"] == 2

    with cleaned.open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert rows[0]["revenue"] == "2000"

    load_result = load_sqlite(str(cleaned), str(database))
    assert load_result["loaded_rows"] == 1
    with sqlite3.connect(database) as connection:
        assert connection.execute("SELECT COUNT(*) FROM sales").fetchone()[0] == 1

    summary = create_summary(str(cleaned), str(summary_file))
    assert summary["total_revenue"] == 2000
    assert json.loads(summary_file.read_text(encoding="utf-8")) == summary
