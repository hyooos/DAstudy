# Week 05 — 결측값과 범주형 변수 처리

| 날짜 | 데이터 | 발제자 | PR 마감 |
| --- | --- | --- | --- |
| 11.01 (일) | Home Credit (첫 주) | 진서현 (`seohyunjinn`) | 11.04 (수) 23:59 |

> **데이터가 바뀌는 주차입니다.**
> 스터디 전날까지 `application_train.csv`, `HomeCredit_columns_description.csv`를 받아([data/README.md](../data/README.md)) `load_home_credit()`으로 shape (307511, 122)을 확인해주세요.
> 칼럼 설명은 [home_credit.md](../docs/data_dictionary/home_credit.md)를 한 번 훑어와주세요.

## 데이터 선정 이유

Bank의 결측은 `unknown`·-1 몇 개뿐이라 결측 처리의 무게를 느끼기 어렵습니다.
Home Credit은 결측 열이 수십 개이고 종류도 다양합니다. 차가 없어서 비는 `OWN_CAR_AGE`(없음), 정말 모르는 `EXT_SOURCE_1`·`OCCUPATION_TYPE`(진짜 결측), 숫자로 위장한 `DAYS_EMPLOYED` 365243과 `XNA`(코드값)가 모두 있습니다.
"빈칸 있는 행 다 지우기"를 하면 대부분의 행이 사라지는 것도 직접 확인할 수 있습니다.

**분석 포인트**

- `isnull()`에 안 잡히는 결측 찾기 (`describe()`의 최댓값, 범주형의 값 목록)
- 결측 여부 자체가 부도율과 관련 있는지 → 관련 있으면 결측은 지울 대상이 아니라 **정보**
- 결측은 열 하나씩이 아니라 "같이 비는 묶음"(건물 정보)으로 판단
- 삭제·대치 전후의 행 수와 부도율을 반드시 같이 보기

## 케이스

> "심사 데이터 정리 좀 해주세요. 빈칸 많은 열이랑 이상한 값 있는 행은 다 지우고 깔끔하게요." — 여신심사팀장

- **케이스 질문:** 빈칸과 이상한 코드값은 각각 무슨 의미이고, 어떻게 처리해야 하나? 처리 방식에 따라 부도율 결론이 바뀌나?
- **AI에게 먼저:** "이 데이터의 결측치를 처리해줘."

## 과제

### 필수

- [ ] 열별 결측 비율표(상위 20개) + `HomeCredit_columns_description.csv`로 각 열의 의미 확인
- [ ] 숨은 결측 찾기: `DAYS_EMPLOYED`의 최댓값, `CODE_GENDER`·`ORGANIZATION_TYPE`의 `XNA`, `NAME_FAMILY_STATUS`의 `Unknown` 개수 → [home_credit.md](../docs/data_dictionary/home_credit.md) 하단 표
- [ ] 결측 여부별 부도율: `EXT_SOURCE_1`, `EXT_SOURCE_3`, `OCCUPATION_TYPE`, `DAYS_EMPLOYED == 365243` 각각 결측인 그룹 vs 아닌 그룹 → 결측이 무작위인지 판단
- [ ] `FLAG_OWN_CAR` × `OWN_CAR_AGE` 결측 교차표 → 구조적 결측("없음") 확인
- [ ] 팀장 요청대로 (a) 결측 있는 행 전부 삭제 (b) 결측 50% 이상 열 삭제를 각각 했을 때 남는 행·열 수와 부도율
- [ ] 범주형 인코딩: `NAME_EDUCATION_TYPE` 순서형 vs 원-핫, `ORGANIZATION_TYPE`(58범주) 원-핫 vs 빈도 인코딩 장단점

### 심화

- [ ] `DAYS_EMPLOYED == 365243`인 신청자의 `NAME_INCOME_TYPE` 분포 → 이 코드의 의미를 추론하고 처리 방식 결정
- [ ] 건물 정보 열들의 결측이 함께 움직이는지 (결측 여부끼리의 상관 또는 `missingno` 히트맵)
- [ ] `EXT_SOURCE_1`을 중앙값 대치 / 결측 플래그 + 대치 / 그대로(NaN) 세 방식으로 두고 부도율과의 관계 비교

## 토론 질문

- "빈칸 많은 열은 다 지우라"를 그대로 따르면 어떤 정보를 잃게 될까? (결측 자체가 신호일 때)
- 결측을 "모른다"로 둘지, "없다"로 바꿀지, 채울지는 무엇을 기준으로 정해야 할까?

## 이번 주에 쌓을 것

- `common/load_data.py` — `load_home_credit()` 확정
- `common/home_credit/preprocess.py` — `fix_days_employed()`, `add_missing_flags()` (6주차와 같은 날이라 **스터디 전날까지** merge)
- `docs/decisions.md` — D-005 [hc] 결측·코드값 처리 결정
- `docs/audit_checklist.md` — "숨은 결측(코드값·XNA)을 확인했는가?", "결측 여부 자체가 타깃과 관련 있는지 봤는가?", "결측 처리 방식에 따라 결론이 바뀌는지 비교했는가?"
- Git 연습 — `common/` 코드 PR에 리뷰어가 Request changes → 수정 후 Approve

## 진행 가이드

### 도입 — Pima Indians Diabetes (10분)

1. `isnull().sum()` → 전부 0이라 "결측 없음"처럼 보임
2. 혈압·BMI·인슐린의 최솟값 확인 → 0 = 살아있는 사람에게 불가능한 값 = 숫자로 위장한 결측
3. "Home Credit에도 이렇게 위장한 값이 있을까?" 질문으로 본 분석 시작 (→ `DAYS_EMPLOYED` 365243, `XNA`)

### Home Credit에서 유의해서 볼 것

- 결측 비율 상위는 건물 정보 열이 거의 다 차지함. 이 열들은 AVG/MODE/MEDI 3종이 같은 행에서 같이 비어 있음 → 열 하나씩이 아니라 **묶음**으로 판단
- `DAYS_EMPLOYED` 최댓값 365243일 ≈ 1,000년 → `describe()`의 max만 봐도 발견 가능. 이 값을 가진 행의 `NAME_INCOME_TYPE`을 보면 의미가 보임 (대부분 연금 수령자)
- `ORGANIZATION_TYPE == "XNA"`와 `DAYS_EMPLOYED == 365243`이 같은 행들인지 교차 확인 → 같은 이유로 생긴 결측이면 처리도 같이
- 결측 그룹의 부도율이 다르면 결측은 무작위가 아님 → 채워버리면 그 신호가 사라짐. 결측 플래그를 따로 남기는 이유
- "결측 있는 행 전부 삭제"를 하면 건물 정보 때문에 대부분의 행이 사라짐 → 남은 행이 어떤 신청자인지(부도율, 주거 형태) 반드시 확인
- `NAME_EDUCATION_TYPE` 순서: Lower secondary < Secondary / secondary special < Incomplete higher < Higher education < Academic degree
- 칼럼 설명 파일은 `encoding="latin-1"`로 읽기 (기본값이면 UnicodeDecodeError) → `load_home_credit_columns()` 사용

### AI 검증 포인트

- `isnull()` 비율만 보고 365243·`XNA`를 놓치는지
- 결측을 일괄 중앙값·최빈값으로 채우는지
- 결측 여부와 부도율의 관계를 보지 않는지
- "50% 이상 결측 열 삭제" 같은 규칙을 근거 없이 쓰는지

### 발제자 준비

- 첫 Home Credit 주차라 D-7에 [home_credit.md](../docs/data_dictionary/home_credit.md)를 공유하고 전원 스터디 전날까지 다운로드·shape 확인
- 전처리 함수 초안을 일부러 "결측 있는 행 전부 삭제" 버전으로 PR → 리뷰어가 Request changes 하도록 (Git 연습과 연결)

## 보조 데이터 (선택)

| 데이터 | 출처 | 해볼 것 |
| --- | --- | --- |
| House Prices | Kaggle 대회 | `PoolQC`, `Alley` 등의 NA는 "없음"(구조적 결측), `LotFrontage`는 진짜 결측 → data_description.txt를 읽고 변수별로 처리 방식 나누기 |
| Pima Indians Diabetes | Kaggle | 혈압·BMI·인슐린이 0인 행 = 숫자로 위장한 결측. `isnull()`은 0개지만 실제로는 상당수 |
| Telco Customer Churn | Kaggle | `TotalCharges`가 문자열로 읽히는 이유(빈 칸) 찾기 → 빈 칸인 고객들의 공통점으로 결측의 의미 판단 |
| Titanic | Kaggle 대회 · `sns.load_dataset("titanic")` | `Age` 결측을 평균/중앙값/호칭(Mr, Miss)별로 채울 때 생존율 분석 차이, `Cabin` 결측이 객실 등급과 얼마나 얽혀 있는지 |

---

## 발제자 작성

아래는 발제자가 채워주세요.

### 교재 범위

-

### 개념 정리

<!-- 스터디 전 (D-7 ~ D-2) -->

### 스터디 후 해설

- 질문:
- 함정:
- 해설:
