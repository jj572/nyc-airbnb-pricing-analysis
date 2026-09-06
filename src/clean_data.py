"""
NYC Airbnb listings data cleaning script.

Drops listings with missing price, and flags the top 1% of prices
as a luxury segment before saving the cleaned data.
"""
import pandas as pd

RAW_PATH = "data/raw/listings.csv"
PROCESSED_PATH = "data/processed/listings_clean.csv"


def main():
    df = pd.read_csv(RAW_PATH)
    print(f"Original row count: {len(df)}")

    df_clean = df.dropna(subset=["price"]).copy()
    print(f"Row count after dropping missing price: {len(df_clean)}")

    threshold = df_clean["price"].quantile(0.99)
    print(f"Top 1% threshold (99th percentile): ${threshold:.2f}")

    df_clean["segment"] = df_clean["price"].apply(
        lambda p: "luxury" if p >= threshold else "mainstream"
    )
    print(df_clean["segment"].value_counts())

    df_clean.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved to {PROCESSED_PATH}")


if __name__ == "__main__":
    main()