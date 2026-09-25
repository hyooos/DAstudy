# Week 07 — 과적합, 교차검증, 데이터 누수

| 날짜 | 데이터 | 발제자 | PR 마감 |
| --- | --- | --- | --- |
| 2026.11.07 (토) | 🏦 Bank Marketing (다시) | @ | 11.11 (수) 23:59 |

> ⚠️ **데이터가 바뀌는 주차** — 다시 🏦 Bank. 4주차 `common/bank/preprocess.py`의 `add_prev_contact_flag()`를 적용한 데이터로 모델링합니다.

## 🎯 사용 데이터: 🏦 Bank Marketing (다시)

**왜 이 데이터?** `duration`이라는, 데이터 제공처가 공식적으로 명시한 누수 변수가 있고, 행이 시간순이라 무작위 분할과 시간순 분할의 차이가 크게 드러남. Home Credit은 신청 날짜가 없어서 시간순 검증을 할 수 없기 때문에 이 주제는 bank가 가장 적합함. 1주차에 정한 예측 시점(D-001)을 여기서 검증.

**유의깊게 봤으면 하는 것**

- 분할 방식이 "내년 캠페인에 쓴다"는 실제 사용 상황과 같은가
- 전처리가 Pipeline 안에서 train에만 fit되는가
- 시간순 분할에서 train·test 가입률이 얼마나 다른가

---

> 📩 "외부 업체가 AUC 0.9짜리 가입 예측 모델을 만들어 왔어요. 바로 도입해도 될까요?" — 마케팅팀장

**케이스 질문:** 이 모델의 검증 점수는 믿을 만한가?

**AI에게 먼저:** "가입 여부를 예측하는 로지스틱 회귀 모델을 만들고 성능을 알려줘."

## 필수 과제

- [ ] `common/bank/preprocess.py`(4주차 `add_prev_contact_flag()`, `unknown`은 하나의 범주로 유지)를 적용한 데이터로 로지스틱 회귀 학습 (`Pipeline` 사용)
- [ ] `duration` 포함 / 제외 모델의 AUC 비교
- [ ] **무작위 분할 vs 시간순 분할**(앞 80% 학습, 뒤 20% 평가) AUC 비교 + 두 분할의 train·test 가입률 비교
- [ ] 5-fold 교차검증: 섞어서(shuffle) 나눈 경우와 섞지 않고 순서대로 나눈 경우의 fold별 점수

## 심화 과제

- [ ] 스케일러·인코더를 분할 전 전체 데이터에 fit한 버전과 Pipeline 버전 비교 (차이가 작더라도 왜 원칙적으로 틀렸는지 설명)
- [ ] Random Forest의 train AUC와 test AUC 차이 → 로지스틱과 비교해 과적합 판단

## 토론 질문

- 외부 업체의 AUC 0.9는 어떤 조건에서 나온 숫자일 가능성이 클까? 업체에게 무엇을 물어봐야 할까?
- 이 모델을 내년 캠페인에 쓴다면 어떤 분할 방식이 실제 사용 상황과 가까울까?

## 이번 주에 쌓을 것

- `common/evaluate.py` `make_pipeline()`, `time_split()`
- `docs/decisions.md` **D-007 [bank]** "분할은 시간순 / 전처리는 Pipeline 안에서"
- `docs/audit_checklist.md` "예측 시점에 알 수 없는 변수를 썼는가?", "전처리를 train에만 fit했는가?", "분할 방식이 실제 사용 상황과 맞는가?"
- **Git 연습:** 실수로 merge된 커밋을 `git revert`로 되돌리는 PR

## 🔍 진행 가이드 & 유의할 점

### 도입 — Hotel Booking Demand (대조 · 15분)

1. `reservation_status` 포함해서 로지스틱 회귀 → AUC가 거의 1
2. 값을 보면 Canceled / Check-Out / No-Show = 타깃 그 자체
3. 빼고 다시 돌리면 점수 급락. 이어서 `booking_changes`, `assigned_room_type`, `days_in_waiting_list`처럼 예약 이후에 바뀔 수 있는 변수도 의심해보기
4. "bank의 `duration`은 이것보다 덜 노골적인데 왜 여전히 누수인가?"로 연결

### bank에서 유의해서 볼 것

- 시간순 분할 시 뒤쪽 행일수록 가입률이 높아서 train과 test 가입률이 크게 다름 → AUC만 보지 말고 두 구간의 가입률을 반드시 같이 보고
- `KFold(shuffle=False)`는 순서대로 자를 뿐 "과거로 미래 예측"이 아님 (뒤 fold가 앞 fold의 train이 됨) → 시간 순서를 지키려면 `TimeSeriesSplit`
- Pipeline: `ColumnTransformer`(스케일러+원핫) + `LogisticRegression`을 하나로 묶고 `cross_val_score`에 Pipeline을 통째로 넣기. 분할 전 `fit_transform` 금지
- 원핫에 `handle_unknown="ignore"` 설정 → 시간순 분할에서 test에만 나오는 범주 대비
- `max_iter` 수렴 경고가 뜨면 스케일링 누락 신호
- `duration` 포함 모델의 AUC가 크게 올라가는 걸 확인 → 외부 업체 AUC 0.9의 정체를 추정하는 근거

### AI 검증 포인트

AI는 거의 항상 `train_test_split(random_state=42)` 무작위 분할 + `duration` 포함 → 이 두 가지를 짚었는지

### 발제자 준비

누수 모델(`duration` 포함 + 무작위 분할 + 전체 데이터에 fit한 스케일러)을 "외부 업체 모델"로 만들어 결과만 공개

## 📦 보조 데이터 (선택)

| 데이터 | 링크 | 해볼 것 |
| --- | --- | --- |
| Hotel Booking Demand | Kaggle | `reservation_status`가 취소 여부를 그대로 담고 있는 완전 누수 → 넣은 모델과 뺀 모델 비교. 도착 날짜 기준 시간순 분할 |
| Rossmann Store Sales | Kaggle 대회 | 학습 데이터에는 있는데 테스트에는 없는 `Customers`(당일 방문객 수) → 예측 시점에 알 수 없는 변수를 대회 설계가 어떻게 막았는지 |
| Seoul Bike Sharing Demand | UCI | 시간별 데이터를 무작위로 나누면 바로 앞뒤 시간이 train·test에 갈라져 점수가 부풀려짐 → 무작위 vs 시간순 분할 점수 비교 |

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
