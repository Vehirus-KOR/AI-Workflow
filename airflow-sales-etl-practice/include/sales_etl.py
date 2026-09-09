import csv
import json
import sqlite3
from pathlib import Path


def clean_sales(input_path: str, output_path: str) -> dict:
    """Keep completed, positive-quantity sales and calculate revenue."""
    source = Path(input_path)
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    cleaned = []
    rejected = 0

    with source.open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                quantity = int(row["quantity"])
                unit_price = int(row["unit_price"])
            except (KeyError, TypeError, ValueError):
                rejected += 1
                continue

            if row.get("status") != "completed" or quantity <= 0 or unit_price <= 0:
                rejected += 1
                continue

            cleaned.append(
                {
                    "order_id": row["order_id"],
                    "order_date": row["order_date"],
                    "category": row["category"],
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "revenue": quantity * unit_price,
                }
            )

    columns = [
        "order_id",
        "order_date",
        "category",
        "quantity",
        "unit_price",
        "revenue",
    ]
    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(cleaned)

    return {"cleaned_path": str(destination), "accepted": len(cleaned), "rejected": rejected}


def load_sqlite(cleaned_path: str, database_path: str) -> dict:
    """Idempotently replace the sales table with the latest cleaned data."""
    database = Path(database_path)
    database.parent.mkdir(parents=True, exist_ok=True)

    with Path(cleaned_path).open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    with sqlite3.connect(database) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                order_id TEXT PRIMARY KEY,
                order_date TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price INTEGER NOT NULL,
                revenue INTEGER NOT NULL
            )
            """
        )
        connection.execute("DELETE FROM sales")
        connection.executemany(
            "INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)",
            [
                (
                    row["order_id"],
                    row["order_date"],
                    row["category"],
                    int(row["quantity"]),
                    int(row["unit_price"]),
                    int(row["revenue"]),
                )
                for row in rows
            ],
        )

    return {"database_path": str(database), "loaded_rows": len(rows)}


def create_summary(cleaned_path: str, summary_path: str) -> dict:
    """Create category totals and a pipeline summary JSON file."""
    totals = {}
    total_revenue = 0

    with Path(cleaned_path).open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    for row in rows:
        revenue = int(row["revenue"])
        category = row["category"]
        totals[category] = totals.get(category, 0) + revenue
        total_revenue += revenue

    summary = {
        "row_count": len(rows),
        "total_revenue": total_revenue,
        "revenue_by_category": totals,
    }
    destination = Path(summary_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary
