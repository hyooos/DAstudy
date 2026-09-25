"""공통 데이터 3개 불러오기.

- load_bank()        : week03에서 확정 (1·2·3·4·7·8주차)
- load_home_credit() : week05에서 확정 (5·6·10주차, 9주차 비교)
- load_cookie_cats() : week09에서 확정 (9주차)

수정할 때는 PR 리뷰 필수.
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def _read(filename, expected_shape, check_shape, **read_kwargs):
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"{path} 가 없습니다. data/README.md를 보고 내려받으세요.")

    df = pd.read_csv(path, **read_kwargs)

    if check_shape and df.shape != expected_shape:
        raise ValueError(
            f"{filename}의 shape이 {df.shape}입니다. 기대값 {expected_shape}. "
            "다른 버전의 파일이 아닌지 확인하세요."
        )
    return df


def load_bank(check_shape=True):
    """🏦 bank-full.csv — (45211, 17), 구분자 ';'.

    bank-additional-full.csv(거시변수 추가, balance 없음)와 헷갈리지 않게 shape을 확인한다.
    """
    return _read("bank-full.csv", (45211, 17), check_shape, sep=";")


def load_home_credit(check_shape=True):
    """💳 application_train.csv — (307511, 122).

    이 스터디는 이 파일만 사용 (bureau 등 보조 테이블, application_test는 X).
    """
    return _read("application_train.csv", (307511, 122), check_shape)


def load_home_credit_columns():
    """💳 HomeCredit_columns_description.csv — 열 설명. latin-1이 아니면 UnicodeDecodeError."""
    return _read(
        "HomeCredit_columns_description.csv", None, False, encoding="latin-1", index_col=0
    )


def load_cookie_cats(check_shape=True):
    """🐱 cookie_cats.csv — (90189, 5)."""
    return _read("cookie_cats.csv", (90189, 5), check_shape)
