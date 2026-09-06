"""
정제된 리스팅 데이터를 SQLite 데이터베이스로 만드는 스크립트
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

    print(f"{DB_PATH} 에 listings 테이블 생성 완료 ({len(df)}행)")


if __name__ == "__main__":
    main()