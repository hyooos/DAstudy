# 💳 Home Credit 변수 사전 — `application_train.csv`

사용 주차: 5·6·10 (+9 보조). 발제자가 5주차 D-7에 이 표를 한 번 더 공유합니다.

| 항목 | 내용 |
| --- | --- |
| 출처 | Kaggle 대회 Home Credit Default Risk — 소비자 대출(현금 대출·리볼빙) 신청자 정보와 이후 상환 결과 |
| 파일 | `application_train.csv` — 307,511행 × 122열. **이 스터디는 이 파일만 사용** (bureau 등 보조 테이블 X, `application_test`는 타깃이 없어서 X) |
| 타깃 | `TARGET` — 1 = 상환 어려움(연체), 약 8.1% |
| 불러오기 | `common.load_data.load_home_credit()` / 열 설명: `load_home_credit_columns()` (`encoding="latin-1"`) |
| 주의 | **신청 날짜가 없음** → 시간순 분할 불가. `DAYS_*` 열은 신청일 기준 며칠 전인지를 **음수**로 기록. **승인된 대출만** 있어서 거절된 신청자는 타깃이 없음 (선택 편향) |

| 변수 그룹 | 대표 열 | 설명 | 주의할 점 |
| --- | --- | --- | --- |
| ID·타깃 | `SK_ID_CURR`, `TARGET` | 신청 ID, 상환 어려움 여부 | ID는 분석 변수로 쓰지 않기 |
| 계약 | `NAME_CONTRACT_TYPE` | Cash loans / Revolving loans | 대부분 현금 대출 |
| 인구통계 | `CODE_GENDER`, `DAYS_BIRTH`, `CNT_CHILDREN`, `CNT_FAM_MEMBERS`, `NAME_FAMILY_STATUS` | 성별, 나이(음수 일수), 자녀·가족 수, 혼인 상태 | `CODE_GENDER`에 `XNA` 몇 건. 나이는 `-DAYS_BIRTH / 365`. 자녀 수와 가족 수는 겹치는 정보 |
| 학력·소득·직업 | `NAME_EDUCATION_TYPE`, `NAME_INCOME_TYPE`, `OCCUPATION_TYPE`, `ORGANIZATION_TYPE`, `AMT_INCOME_TOTAL` | 학력(5단계), 소득 유형, 직업, 소속 기관 종류, 연소득 | 학력은 서열척도. `OCCUPATION_TYPE` 약 31% 결측. `ORGANIZATION_TYPE`은 58범주에 `XNA` 포함. **소득은 오른쪽 꼬리가 극단적으로 김** |
| 재직 | `DAYS_EMPLOYED` | 재직 기간(음수 일수) | **365243 = 코드값** (약 18%, 대부분 연금 수령자) → 5·6주차 핵심 |
| 대출 조건 | `AMT_CREDIT`, `AMT_ANNUITY`, `AMT_GOODS_PRICE` | 대출액, 연간 상환액, 구매 대상 상품 가격 | `AMT_CREDIT`–`AMT_GOODS_PRICE` 상관 약 0.99 (10주차) |
| 자산 | `FLAG_OWN_CAR`, `OWN_CAR_AGE`, `FLAG_OWN_REALTY` | 차·부동산 보유 여부, 차량 연식 | 차가 없으면 `OWN_CAR_AGE`가 비어 있음 = **구조적 결측** |
| 주거·지역 | `NAME_HOUSING_TYPE`, `REGION_POPULATION_RELATIVE`, `REGION_RATING_CLIENT`, `REGION_RATING_CLIENT_W_CITY`, `REG_*`·`LIVE_*` | 주거 형태, 지역 인구 비율, 지역 등급(1~3), 주소 불일치 플래그 | 지역 등급 두 열은 거의 같은 정보 |
| 외부 신용점수 | `EXT_SOURCE_1`, `EXT_SOURCE_2`, `EXT_SOURCE_3` | 외부 기관 점수(0~1로 정규화) | 가장 강한 예측변수. `_1`은 절반 넘게 결측, `_3`도 약 20% 결측 |
| 건물 정보 (47열) | `APARTMENTS_AVG`, `APARTMENTS_MODE`, `APARTMENTS_MEDI` 등 | 거주 건물 특성의 평균·최빈값·중앙값 | 같은 항목이 3종 세트 → 결측도 같이 비고 공선성도 큼. 대부분 절반 이상 결측 |
| 신청 과정 | `WEEKDAY_APPR_PROCESS_START`, `HOUR_APPR_PROCESS_START` | 신청 요일·시각 | 시각은 숫자지만 순환형 |
| 연락·서류 플래그 | `FLAG_MOBIL`, `FLAG_EMP_PHONE` 등, `FLAG_DOCUMENT_2`~`_21` | 연락처 제공, 서류 제출 여부 | 대부분 한쪽 값만 있어 분산이 거의 없음 |
| 주변인 연체 | `OBS_30_CNT_SOCIAL_CIRCLE`, `DEF_30_CNT_SOCIAL_CIRCLE`, `OBS_60_…`, `DEF_60_…` | 주변인 중 연체가 관측된 수 | 30일·60일 기준이 거의 같은 정보 |
| 신용조회 | `AMT_REQ_CREDIT_BUREAU_HOUR` ~ `_YEAR` | 신청 전 기간별 신용조회 횟수 | 약 13% 결측 |
| 기타 날짜 | `DAYS_REGISTRATION`, `DAYS_ID_PUBLISH`, `DAYS_LAST_PHONE_CHANGE` | 등록·신분증 발급·전화 변경 후 경과 일수 | 모두 음수 일수 |

## 숨은 결측·코드값 정리 (week05에서 채우기)

| 열 | 값 | 개수 / 비율 | 의미 (추론) | 처리 (D-005) |
| --- | --- | --- | --- | --- |
| `DAYS_EMPLOYED` | 365243 |  |  |  |
| `CODE_GENDER` | `XNA` |  |  |  |
| `ORGANIZATION_TYPE` | `XNA` |  |  |  |
| `NAME_FAMILY_STATUS` | `Unknown` |  |  |  |
| `OWN_CAR_AGE` | NaN (차 없음) |  | 구조적 결측 |  |
