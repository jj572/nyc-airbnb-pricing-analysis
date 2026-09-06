"""
NYC Airbnb 리스팅 데이터 정제 스크립트

price가 비어있는 리스팅을 제외하고 정제된 데이터를 저장한다
"""
import pandas as pd

RAW_PATH = "data/raw/listings.csv"
PROCESSED_PATH = "data/processed/listings_clean.csv"


def main():
    df = pd.read_csv(RAW_PATH)
    print(f"원본 행 개수: {len(df)}")

    df_clean = df.dropna(subset=["price"]).copy()
    print(f"price 있는 행만 남긴 뒤 행 개수: {len(df_clean)}")

    df_clean.to_csv(PROCESSED_PATH, index=False)
    print(f"{PROCESSED_PATH} 저장 완료")


if __name__ == "__main__":
    main()