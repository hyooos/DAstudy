# 2026-2 데이터 분석 스터디

교재 **「데이터 분석가가 반드시 알아야 할 모든 것」** 을 읽고, **UCI Bank Marketing `bank-full.csv` 하나로 10주 동안** 분석하는 스터디입니다.
같은 데이터를 계속 쓰기 때문에 공용 코드(`common/`)와 결정 기록(`docs/decisions.md`)을 매주 쌓아 갑니다.

- 노션: <!-- TODO: 노션 링크 -->

## 개요

| 항목 | 내용 |
| --- | --- |
| 교재 | 데이터 분석가가 반드시 알아야 할 모든 것 |
| 데이터 | UCI Bank Marketing `bank-full.csv` (10주 내내 같은 데이터) + 주차별 보조 데이터(선택) |
| 메인 모델 | Logistic Regression (7~8주차에 Random Forest를 비교용으로만) |
| 숙제 | ① 교재 해당 범위 읽기 ② 모임 후 D+3(수) 23:59까지 분석 PR 제출 |
| 스터디 | 같은 자리에서 **각자 먼저** 분석 → 결과 비교·토론 → AI 결과와 비교 |
| 스터디 후 | 분석 노트북을 PR로 제출 → 서로 리뷰 → merge |

## 멤버

폴더 이름은 **GitHub 아이디**를 씁니다 (한글·띄어쓰기·대문자 X).

| GitHub 아이디 | 이름 | 비고 |
| --- | --- | --- |
| `github-id` | 이름 | 운영 |
| `github-id` | 이름 |  |

## 커리큘럼

| 주차 | 날짜 | 주제 | 폴더 | 발제자 |
| --- | --- | --- | --- | --- |
| 1 | 09.13 | 분석 목적 도출과 목적의 전환 (소급 정리) | [week01_problem-definition](week01_problem-definition/) |  |
| 2 | 09.20 | 통계의 기초, 표본과 편향 (소급 정리) | [week02_sampling-bias](week02_sampling-bias/) |  |
| 3 | 09.27 | 변수와 척도, 기술통계, 심슨의 역설 | [week03_scales-descriptive](week03_scales-descriptive/) |  |
| 4 | 10.04 | 데이터 탐색과 상관분석 | [week04_eda-correlation](week04_eda-correlation/) |  |
| 5 | 11.01 | 결측값과 범주형 변수 처리 | [week05_missing-categorical](week05_missing-categorical/) |  |
| 6 | 11.01 | 이상치와 분포 확인 | [week06_outliers-distribution](week06_outliers-distribution/) |  |
| 7 | 11.07 | 과적합, 교차검증, 데이터 누수 | [week07_overfitting-leakage](week07_overfitting-leakage/) |  |
| 8 | 11.08 | 클래스 불균형과 분류 성능 평가 | [week08_imbalance-evaluation](week08_imbalance-evaluation/) |  |
| 9 | 11.15 | 가설검정과 검증 설계 | [week09_hypothesis-testing](week09_hypothesis-testing/) |  |
| 10 | 11.22 (비대면) | 다중공선성, 데이터 마사지와 분석가의 판단 | [week10_multicollinearity-judgment](week10_multicollinearity-judgment/) |  |

모든 케이스는 **"은행 마케팅팀이 분석가에게 보낸 요청"** 이라는 설정입니다.
요청을 통계 문제로 번역하고 → AI에게 먼저 시켜본 뒤 → AI 답변을 검증하는 흐름으로 진행합니다. 과제는 **필수**를 먼저, 시간이 남으면 **심화**.

## 폴더 구조

```
2026-2-data-analysis-study/
├── README.md
├── requirements.txt
├── .github/                      # PR·Issue 템플릿
├── data/README.md                # 데이터 다운로드 방법 (csv는 커밋하지 않음)
├── common/                       # 공용 코드 (PR 리뷰 필수)
│   ├── load_data.py
│   ├── preprocess.py
│   └── evaluate.py
├── docs/                         # 공용 문서 (PR 리뷰 필수)
│   ├── data_dictionary.md
│   ├── decisions.md
│   └── audit_checklist.md
├── templates/worksheet.md
└── weekNN_주제/
    ├── README.md                 # 케이스·과제 / 발제자: 개념 정리 + 모임 후 해설
    ├── presenter/                # 발표 자료, 발제자가 준비한 실습 자료
    ├── <github-id>/              # 각자 폴더
    │   ├── worksheet.md
    │   ├── analysis.ipynb
    │   └── extra_<데이터명>.ipynb  # 보조 데이터 (선택)
    └── summary.md                # 각자 인사이트 한 줄씩
```

## 처음 세팅

```bash
# 1. GitHub에서 이 레포를 fork 한 뒤
git clone https://github.com/<내-아이디>/2026-2-data-analysis-study.git
cd 2026-2-data-analysis-study
git remote add upstream https://github.com/<원본-아이디>/2026-2-data-analysis-study.git

# 2. 가상환경 + 패키지
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. 노트북 출력 자동 제거 (커밋할 때 출력이 빠짐)
nbstripout --install

# 4. 데이터 받기 → data/README.md 참고
```

노트북에서 공용 코드 불러오기 (`weekNN/<아이디>/analysis.ipynb` 기준):

```python
import sys
sys.path.append("../..")
from common.load_data import load_bank

df = load_bank()          # shape (45211, 17) 확인까지 해 줌
```

## 매주 진행 흐름

| 시점 | 누가 | 할 일 |
| --- | --- | --- |
| D-7 | 발제자 | 주차 Issue 등록, 리뷰 배정 |
| D-7 ~ D-2 | 발제자 | 주차 폴더 `README.md`(범위, 개념 정리)와 발표 자료 올리기 |
| D-7 ~ D-1 | 전원 | 교재 읽기 |
| D-1 | 전원 | fork 최신화 + 작업 브랜치 생성 |
| D | 전원 | 모임에서 본인 폴더에 분석, 워크시트 작성, 로컬 커밋 |
| D | 발제자 | 모임 후 README에 케이스 **질문·함정·해설** 추가, `decisions.md` PR |
| D+3 (수) 23:59 | 전원 | 개인 분석 PR 제출 |

```bash
# D-1: fork 최신화 + 브랜치
git checkout main
git pull upstream main
git push origin main
git checkout -b week03-<아이디>
```

## 커밋·PR 규칙

**커밋 메시지:** `weekN: 종류 - 뭘했는지`

| 종류 | 언제 | 예시 |
| --- | --- | --- |
| `add` | 새 분석·파일 추가 | `week03: add - balance 대표값 비교표` |
| `fix` | 잘못된 코드·해석 수정 | `week03: fix - pdays -1 제외하고 평균 다시 계산` |
| `review` | 리뷰 반영 | `week03: review - 중앙값 선택 근거 워크시트에 추가` |
| `refactor` | 결과는 같고 코드만 정리 | `week05: refactor - 결측 비율 계산을 함수로 분리` |
| `docs` | md 문서 수정 | `week03: docs - summary.md 인사이트 추가` |

**PR 제목**

| 종류 | 형식 | 예시 |
| --- | --- | --- |
| 개인 분석 | `[weekNN] 이름 - 핵심 결론 한 줄` | `[week03] 효원 - 가입자 나이는 평균과 중앙값이 반대 방향` |
| 공용 코드 | `[common] 함수명 추가/수정` | `[common] clean_unknown() 추가` |
| 보조 데이터 | `[weekNN-extra] 이름 - 데이터명` | `[week05-extra] 효원 - Pima의 0값 결측` |

PR 본문은 템플릿(`.github/pull_request_template.md`)이 자동으로 뜹니다.

**PR 올리기 전에 확인**

```bash
git status                 # 내 폴더(또는 합의된 공용 파일)만 바뀌었는지
git diff --stat            # 바뀐 파일 목록과 양
git log --oneline -5       # 커밋 메시지
```

## LLM 사용 규칙

- 코드 문법, 에러는 자유
- 방법 선택과 해석은 **본인 워크시트에 먼저 작성한 뒤에만**
- AI와 달랐던 점을 워크시트와 PR에 기록
- 분석하면서 점검할 항목은 [`docs/audit_checklist.md`](docs/audit_checklist.md)
