"""💳 Home Credit 전처리 (5·6·10주차).

결정(docs/decisions.md의 [hc] 항목)이 확정되면 해당 함수를 PR로 채운다.
적용 순서: fix_days_employed() → add_missing_flags() → cap_outliers()
(코드값을 먼저 처리하지 않으면 365243이 이상치로 잡힌다)
수정할 때는 PR 리뷰 필수.
"""


def fix_days_employed(df):
    """week05 / D-005 [hc]: DAYS_EMPLOYED == 365243(코드값, 약 18%) 처리.

    초안: 플래그 열을 만든 뒤 원래 열은 NaN으로. 최종 방식은 week05 모임에서 결정.
    ORGANIZATION_TYPE == 'XNA'와 같은 행인지 함께 확인.
    """
    raise NotImplementedError("week05에서 구현")


def add_missing_flags(df, cols):
    """week05 / D-005 [hc]: 결측 여부가 TARGET과 관련 있는 열에 결측 플래그(<col>_missing) 추가.

    후보: EXT_SOURCE_1, EXT_SOURCE_3, OCCUPATION_TYPE
    """
    raise NotImplementedError("week05에서 구현")


def cap_outliers(df, cols, lower=0.01, upper=0.99):
    """week06 / D-006 [hc]: 지정한 분위수로 상한·하한 처리.

    분위수 경계는 train에서만 계산해야 함 (week07 Pipeline 원칙).
    fix_days_employed()를 먼저 적용한 데이터에 쓴다.
    """
    raise NotImplementedError("week06에서 구현")
