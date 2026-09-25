# data/

데이터 파일은 **커밋하지 않습니다** (`.gitignore`에서 막혀 있음). 각자 내려받아 이 폴더에 두세요.

```
data/
├── README.md
├── bank-full.csv                        # 🏦 1주차 전
├── application_train.csv                # 💳 5주차 D-1까지
├── HomeCredit_columns_description.csv   # 💳
└── cookie_cats.csv                      # 🐱 9주차 D-1까지
```

## 🏦 Bank Marketing — 1·2·3·4·7·8주차

1. [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) 다운로드
2. 압축을 풀면 안에 `bank.zip`이 또 있음 → 그 안의 `bank-full.csv`를 이 폴더로
3. `load_bank()` → shape (45211, 17)

> 같은 zip의 `bank-additional-full.csv`는 거시변수가 추가됐지만 `balance`가 없어 메인으로 쓰지 않음 (7주차 누수 토론 보조용).

## 💳 Home Credit Default Risk — 5·6·10주차 (+9 보조)

1. Kaggle 대회 **Home Credit Default Risk** 페이지에서 **Join Competition**(규칙 동의) 후 Data 탭에서 다운로드
   - 또는 Kaggle API: `kaggle competitions download -c home-credit-default-risk`
2. 압축에서 **`application_train.csv`, `HomeCredit_columns_description.csv` 두 개만** 이 폴더로 (나머지 테이블은 안 씀)
3. `load_home_credit()` → shape (307511, 122)
4. 열 설명은 `load_home_credit_columns()` (내부에서 `encoding="latin-1"`)

## 🐱 Cookie Cats A/B Test — 9주차

1. Kaggle에서 "Cookie Cats" A/B 테스트 데이터셋 다운로드
2. `cookie_cats.csv`를 이 폴더로
3. `load_cookie_cats()` → shape (90189, 5)

## 보조 데이터

주차별 보조 데이터는 각 `weekNN_*/README.md` 하단 참고. 받은 파일도 이 폴더에 두고 커밋하지 않습니다.
