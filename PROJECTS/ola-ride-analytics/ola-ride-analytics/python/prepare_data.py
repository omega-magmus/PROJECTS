"""Convert the raw Excel workbook into a clean CSV that MySQL / Power BI can load.

Usage (from repo root):  python python/prepare_data.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "Bookings-100000-Rows.xlsx"
OUT = ROOT / "data" / "bookings.csv"

df = pd.read_excel(SRC)

# The last column is completely empty in the source file.
df = df.drop(columns=["Vehicle Images"], errors="ignore")

# Keep a pure date plus a separate time string.
df["Date"] = pd.to_datetime(df["Date"]).dt.date
df["Time"] = df["Time"].astype(str)

df.to_csv(OUT, index=False)
print(f"Wrote {len(df):,} rows x {df.shape[1]} columns -> {OUT.relative_to(ROOT)}")
