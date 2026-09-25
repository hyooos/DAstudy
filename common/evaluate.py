"""공용 모델링·평가 함수 (7·8주차, 데이터 공통).

결정(docs/decisions.md)이 확정되면 해당 함수를 PR로 채운다.
수정할 때는 PR 리뷰 필수.
"""


def make_pipeline(num_cols, cat_cols, model=None):
    """week07 / D-007: ColumnTransformer(스케일러 + 원핫) + 모델을 하나의 Pipeline으로.

    - 전처리는 반드시 Pipeline 안에서 train에만 fit
    - OneHotEncoder(handle_unknown="ignore") — 시간순 분할에서 test에만 나오는 범주 대비
    """
    raise NotImplementedError("week07에서 구현")


def time_split(df, train_frac=0.8):
    """week07 / D-007: 행 순서(= 시간순) 기준 앞 train_frac은 train, 나머지는 test.

    Bank 전용 (Home Credit은 신청 날짜가 없어 시간순 분할 불가).
    """
    raise NotImplementedError("week07에서 구현")


def report_classification(y_true, y_prob, threshold=0.5):
    """week08 / D-008: 혼동행렬, 정밀도, 재현율, F1, ROC-AUC, PR-AUC(+기준선 = 양성 비율) 한 번에."""
    raise NotImplementedError("week08에서 구현")


def profit_curve(y_true, y_prob, cost_per_call, gain_per_success):
    """week08: 임계값(또는 상위 k%)별 기대 수익 곡선.

    비용·이익 가정은 스터디원끼리 통일 (예: 1:5, 1:10 두 시나리오).
    """
    raise NotImplementedError("week08에서 구현")
