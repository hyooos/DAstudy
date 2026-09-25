"""🏦 Bank Marketing 전처리 (4·7주차).

결정(docs/decisions.md의 [bank] 항목)이 확정되면 해당 함수를 PR로 채운다.
수정할 때는 PR 리뷰 필수.
"""


def add_prev_contact_flag(df):
    """week04 / D-004 [bank]: pdays == -1 → 이전 연락 여부 플래그(prev_contact) 생성.

    -1은 "이전 연락 없음"을 뜻하는 코드값이라 경과 일수와 분리해야 한다.
    pdays의 -1을 NaN으로 바꿀지 그대로 둘지는 week04 모임에서 결정.
    week07 모델링에서 이 함수를 적용한 데이터를 쓴다 (unknown은 하나의 범주로 유지).
    """
    raise NotImplementedError("week04에서 구현")
