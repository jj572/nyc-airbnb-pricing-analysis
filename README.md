# NYC Airbnb Pricing Analysis

Inside Airbnb의 뉴욕 리스팅 데이터를 SQL과 Python으로 분석하는 프로젝트.
가격에 영향을 주는 요인을 찾고, 호스트/플랫폼 관점에서 프라이싱 인사이트를 도출하는 것이 목표.

## 데이터

- 출처: Inside Airbnb (뉴욕시 리스팅 스크랩 데이터)
- data/raw/listings.csv: 원본 데이터, 수정하지 않음
- data/processed/: 정제된 데이터가 들어갈 폴더

## 폴더 구조

- data/raw/ 원본 데이터, 건드리지 않음
- data/processed/ 정제된 데이터
- sql/ 스키마 및 분석 쿼리
- notebooks/ 탐색적 분석, 시각화
- src/ 재사용하는 파이썬 함수
- outputs/figures/ 저장한 그래프 이미지

## 실행 환경

pip install -r requirements.txt