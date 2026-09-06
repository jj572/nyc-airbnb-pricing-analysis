"""
Loads the cleaned listings data into a SQLite database.
"""
import sqlite3
import pandas as pd

CSV_PATH = "data/processed/listings_clean.csv"
DB_PATH = "data/processed/airbnb.db"


def main():
    df = pd.read_csv(CSV_PATH)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("listings", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Created listings table in {DB_PATH} ({len(df)} rows)")


if __name__ == "__main__":
    main()