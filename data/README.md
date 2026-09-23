# data/

데이터 파일은 **커밋하지 않습니다** (`.gitignore`에서 막혀 있음). 각자 내려받아 이 폴더에 두세요.

## 메인 데이터: `bank-full.csv`

1. [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) 에서 다운로드
2. 압축을 풀면 안에 `bank.zip`이 또 있음 → 그 안의 `bank-full.csv`를 이 폴더로
3. 확인

```python
import pandas as pd
df = pd.read_csv("data/bank-full.csv", sep=";")   # 구분자 세미콜론!
df.shape   # (45211, 17)
```

```
data/
├── README.md
└── bank-full.csv      ← 여기
```

> `bank-additional-full.csv`(41,188행, 21열)는 **다른 버전**이니 헷갈리지 않게 주의.

## 보조 데이터

주차별 보조 데이터 링크는 각 `weekNN_*/README.md` 하단 참고. 받은 파일도 이 폴더에 두고 커밋하지 않습니다.
