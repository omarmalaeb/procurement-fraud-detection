import pandas as pd
from pathlib import Path


def load_data():
    data_dir = Path(__file__).resolve().parent.parent / "archive" / "Procument Invoice Fraud Dataset v1"

    invoices = pd.read_parquet(data_dir / "invoices.parquet")
    labels = pd.read_parquet(data_dir / "labels.parquet")
    suppliers = pd.read_parquet(data_dir / "suppliers.parquet")
    departments = pd.read_parquet(data_dir / "departments.parquet")
    behaviour = pd.read_parquet(data_dir / "behavioural_features.parquet")
    splits = pd.read_parquet(data_dir / "splits.parquet")

    return invoices, labels, suppliers, departments, behaviour, splits

def merge_data(invoices, labels, suppliers, departments, behaviour, splits):
    data = invoices.merge(labels, on="invoice_id")
    data = data.merge(suppliers, on="supplier_id")
    data = data.merge(departments, on="department_id")
    data = data.merge(behaviour, on="invoice_id")
    data = data.merge(splits, on="invoice_id")

    return data