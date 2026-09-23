# Week 05 — 결측값과 범주형 변수 처리

| 날짜 | 발제자 | PR 마감 |
| --- | --- | --- |
| 2026.11.01 (일) | @ | 11.04 (수) 23:59 |

> 📩 "데이터 정리 좀 해주세요. 이상한 값은 다 지우고 깔끔하게요." — 마케팅팀장

**케이스 질문:** `unknown`과 -1을 어떻게 처리해야 하나? 처리 방식에 따라 결론이 바뀌나?

**AI에게 먼저:** "이 데이터의 결측치를 처리해줘."

## 필수 과제

- [ ] `isnull()` 결과와 변수별 `unknown` 비율표를 나란히 놓기
- [ ] `unknown`인 고객과 아닌 고객의 가입률 비교 → 결측이 무작위인지 판단
- [ ] `poutcome == unknown`과 `pdays == -1`의 교차표
- [ ] `job`, `education`, `contact`에 unknown이 하나라도 있는 행을 **삭제**했을 때 전체 가입률 변화
- [ ] 범주형 인코딩 비교: 원-핫 vs 순서형(`education`) — 장단점 정리

## 심화 과제

- [ ] `contact == unknown`의 비율을 **연도별로** 보기 → 이 결측은 왜 생겼을까?
- [ ] `education`의 unknown을 최빈값(secondary)으로 채우는 게 맞는지, 가입률로 판단

## 토론 질문

- "이상한 값은 다 지우라"는 요청을 그대로 따르면 어떤 결론이 왜곡될까?
- 결측을 "모른다"로 둘지, "없다"로 바꿀지, 채울지는 무엇을 기준으로 정해야 할까?

## 이번 주에 쌓을 것

- `common/preprocess.py` `clean_unknown()`, `add_prev_contact_flag()`
- `docs/decisions.md` **D-005** unknown·pdays 처리 결정
- `docs/audit_checklist.md` "숨은 결측(unknown, -1)을 확인했는가?", "결측 처리 방식에 따라 결론이 바뀌는지 비교했는가?"
- **Git 연습:** `common/` 코드 PR에 리뷰어가 Request changes → 수정 후 Approve

## 📦 보조 데이터 (선택)

| 데이터 | 링크 | 해볼 것 |
| --- | --- | --- |
| House Prices | Kaggle 대회 | `PoolQC`, `Alley` 등의 NA는 "없음"(구조적 결측), `LotFrontage`는 진짜 결측 → data_description.txt를 읽고 변수별로 처리 방식 나누기 |
| Pima Indians Diabetes | Kaggle | 혈압·BMI·인슐린이 0인 행 = 숫자로 위장한 결측. `isnull()`은 0개지만 실제로는 상당수 |
| Telco Customer Churn | Kaggle | `TotalCharges`가 문자열로 읽히는 이유(빈 칸) 찾기 → 빈 칸인 고객들의 공통점으로 결측의 의미 판단 |
| Titanic | Kaggle 대회 · `sns.load_dataset("titanic")` | `Age` 결측을 평균/중앙값/호칭(Mr, Miss)별로 채울 때 생존율 분석 차이, `Cabin` 결측이 객실 등급과 얼마나 얽혀 있는지 |

---

## 📝 발제자 작성

### 교재 범위
-

### 개념 정리
<!-- D-7 ~ D-2 -->

### 모임 후 해설
- **질문:**
- **함정:**
- **해설:**
