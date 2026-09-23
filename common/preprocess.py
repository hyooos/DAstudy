"""공용 전처리 함수.

주차별로 결정(docs/decisions.md)이 확정되면 해당 함수를 PR로 채운다.
수정할 때는 PR 리뷰 필수.
"""


def clean_unknown(df):
    """week05 / D-005: unknown·-1 처리 규칙 적용.

    초안 (week05 모임 후 확정):
    - poutcome의 unknown → 'none'
    - job, education, contact의 unknown은 그대로 둘지 결정
    """
    raise NotImplementedError("week05에서 구현")


def add_prev_contact_flag(df):
    """week05 / D-005: pdays == -1 → 이전 연락 여부 플래그(prev_contact) 생성."""
    raise NotImplementedError("week05에서 구현")


def cap_outliers(df, cols, lower=0.01, upper=0.99):
    """week06 / D-006: 지정한 분위수로 상한·하한 처리.

    분위수 경계는 train에서만 계산해야 함 (week07 Pipeline과 연결).
    """
    raise NotImplementedError("week06에서 구현")
