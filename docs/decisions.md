# 결정 기록 (Decision Log)

10주 동안 같은 데이터를 쓰기 때문에, 한 번 정한 처리 방식은 여기에 남기고 이후 주차는 이 기준을 따릅니다.
다르게 처리했다면 개인 워크시트와 PR에 **이유**를 적어 주세요.

- 추가·수정은 발제자가 모임 후 PR로 (리뷰 필수)
- 상태: `예정` → `확정` (바뀌면 `변경` + 날짜와 이유)

## 형식

```markdown
## D-000 제목
- 주차 / 상태: weekNN / 확정
- 결정:
- 이유:
- 검토한 대안:
- 영향: (common 함수, 이후 주차)
```

---

## D-001 예측 시점은 전화 걸기 전
- 주차 / 상태: week01 / 확정 필요
- 결정: 모델은 "전화를 걸기 전에" 누구에게 걸지 정하는 용도. 전화 전에 알 수 없는 변수는 예측에 쓰지 않는다.
- 이유:
- 검토한 대안:
- 영향: `data_dictionary.md` 시점 열, D-004

## D-002 결과는 '연락받은 고객' 기준임을 명시
- 주차 / 상태: week02 / 확정 필요
- 결정: 모든 결과는 은행 전체 고객이 아니라 "캠페인에서 연락받은 고객" 기준으로 서술한다.
- 이유:
- 검토한 대안:
- 영향:

## D-003 치우친 수치 변수는 평균과 중앙값을 함께 보고
- 주차 / 상태: week03 / 예정

## D-004 `duration`은 설명용 분석에만, 예측 모델에서는 제외
- 주차 / 상태: week04 / 예정

## D-005 unknown · pdays 처리
- 주차 / 상태: week05 / 예정
- 영향: `common/preprocess.py` `clean_unknown()`, `add_prev_contact_flag()`

## D-006 이상치 처리
- 주차 / 상태: week06 / 예정
- 영향: `common/preprocess.py` `cap_outliers()`

## D-007 분할은 시간순 / 전처리는 Pipeline 안에서
- 주차 / 상태: week07 / 예정
- 영향: `common/evaluate.py` `make_pipeline()`, `time_split()`

## D-008 주 평가지표
- 주차 / 상태: week08 / 예정
- 영향: `common/evaluate.py` `report_classification()`, `profit_curve()`

## D-009 검정 결과는 p값과 효과 크기를 함께 보고
- 주차 / 상태: week09 / 예정
