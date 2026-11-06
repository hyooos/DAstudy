# data/

**Bank Marketing의 `bank-full.csv`는 저장소에 포함되어 있습니다.** 저장소를 clone하거나 최신 main을 받으면 별도 다운로드 없이 사용할 수 있습니다.
Home Credit, Cookie Cats와 보조 데이터는 기존대로 각자 내려받고 커밋하지 않습니다. `.gitignore`는 Bank 원본 한 파일만 예외로 허용합니다.

```
data/
├── README.md
├── bank-full.csv                        # 🏦 저장소 포함 (공식 원본)
├── application_train.csv                # 💳 5주차 D-1까지
├── HomeCredit_columns_description.csv   # 💳
└── cookie_cats.csv                      # 🐱 9주차 D-1까지
```

## 🏦 Bank Marketing — 1·2·3·4·7·8주차

1. 저장소에 포함된 `data/bank-full.csv` 사용
2. `load_bank()` → shape (45211, 17), 구분자 `;`
3. 원본을 다시 받을 때만 [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing)에서 다운로드 → `bank.zip` 안의 `bank-full.csv` 사용

### 출처와 이용 조건

- 인용: Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. [DOI: 10.24432/C5K306](https://doi.org/10.24432/C5K306).
- 라이선스: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). [UCI 원본 페이지](https://archive.ics.uci.edu/dataset/222/bank+marketing)의 라이선스 안내를 따릅니다.
- 이 파일은 공식 배포본을 수정하지 않고 재배포한 원본입니다. 행 순서, 값, 인코딩과 줄바꿈을 변경하지 않았습니다.
- SHA-256: `d1513ec63b385506f7cfce9f2c5caa9fe99e7ba4e8c3fa264b3aaf0f849ed32d`.

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
