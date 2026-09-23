"""bank-full.csv 불러오기.

week03에서 확정. 수정할 때는 PR 리뷰 필수.
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
EXPECTED_SHAPE = (45211, 17)


def load_bank(path=None, check_shape=True):
    """bank-full.csv를 DataFrame으로 불러온다.

    Parameters
    ----------
    path : str | Path | None
        None이면 레포 루트의 data/bank-full.csv
    check_shape : bool
        True면 (45211, 17)이 아닐 때 에러
    """
    path = Path(path) if path else DATA_DIR / "bank-full.csv"
    if not path.exists():
        raise FileNotFoundError(f"{path} 가 없습니다. data/README.md를 보고 내려받으세요.")

    df = pd.read_csv(path, sep=";")

    if check_shape and df.shape != EXPECTED_SHAPE:
        raise ValueError(
            f"shape이 {df.shape}입니다. 기대값 {EXPECTED_SHAPE}. "
            "bank-additional-full.csv 등 다른 파일이 아닌지 확인하세요."
        )
    return df
