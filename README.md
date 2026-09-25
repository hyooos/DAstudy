# 🐘 2026-2 BOAZ 데이터 분석 스터디

교재 **「데이터 분석가가 반드시 알아야 할 모든 것」** 을 읽고, **공통 데이터 3개**를 주차 주제에 맞게 번갈아 분석하는 10주 스터디입니다.
공용 코드(`common/`)와 분석 내용(`docs/decisions.md`)을 데이터별로 매주 쌓아 갑니다.

## 분석 데이터

10주 동안 분석 데이터 3개를 주차에 맞게 나눠서 사용할 예정입니다.
주차별로 왜 이 데이터를 선정했는지에 대해서는 각 주차의 README를 참고해주세요.
(발제자 재량으로 수정 가능합니다!)

| 데이터 | 주차 | 분석 포인트 | 칼럼 |
| --- | --- | --- | --- |
| Bank Marketing | 1·2·3·4·7·8 | 날짜순 정렬인데 연도 열이 없음(심슨의 역설·시간순 분할), 공식 누수 변수 `duration`, 코드형 결측(-1, unknown), 적당한 불균형(11.7%) | [bank.md](docs/data_dictionary/bank.md) |
| Home Credit | 5·6·10 (+9 보조) | 결측 종류가 다양(구조적·진짜·코드 365243·XNA), 극단 소득, AVG/MODE/MEDI 공선성 묶음, 변수 120개라 다중검정 체감 | [home_credit.md](docs/data_dictionary/home_credit.md) |
| Cookie Cats | 9 | 실제 무작위 배정 A/B 실험 → "검정 결과로 의사결정" 연습 | [cookie_cats.md](docs/data_dictionary/cookie_cats.md) |


## 멤버

폴더 이름은 **Github 아이디**로 통일해주세요.

| GitHub 아이디 | 이름 |
| --- | --- |
| `jjjng-je` | 한정재 |
| `hyooos` | 최효원 |
| `tired-gini` | 형지원 |
| `seohyunjinn` | 진서현 |
| `foresttin` | 이수빈 |
| `lcsvvo` | 김지우 |

## 커리큘럼

| 주차 | 날짜 | 주제 | 데이터 | 폴더 | 발제자 |
| --- | --- | --- | --- | --- | --- |
| 1 | 09.13 | 분석 목적 도출과 목적의 전환 (소급 정리) | Bank Marketing | [week01](week01_problem-definition/) | 전원 |
| 2 | 09.20 | 통계의 기초, 표본과 편향 (소급 정리) | Bank Marketing | [week02](week02_sampling-bias/) | 한정재 |
| 3 | 09.27 | 변수와 척도, 기술통계, 심슨의 역설 | Bank Marketing | [week03](week03_scales-descriptive/) | 최효원 |
| 4 | 10.04 | 데이터 탐색과 상관분석 | Bank Marketing | [week04](week04_eda-correlation/) | 이수빈 |
| 5 | 11.01 | 결측값과 범주형 변수 처리 | Home Credit | [week05](week05_missing-categorical/) | 진서현 |
| 6 | 11.01 | 이상치와 분포 확인 | Home Credit | [week06](week06_outliers-distribution/) | 김지우 |
| 7 | 11.07 | 과적합, 교차검증, 데이터 누수 | Bank Marketing | [week07](week07_overfitting-leakage/) | 형지원 |
| 8 | 11.08 | 클래스 불균형과 분류 성능 평가 | Bank Marketing | [week08](week08_imbalance-evaluation/) | - |
| 9 | 11.15 | 가설검정과 검증 설계 | Cookie Cats + Home Credit | [week09](week09_hypothesis-testing/) | - |
| 10 | 11.22 (비대면) | 다중공선성, 데이터 마사지와 분석가의 판단 | Home Credit | [week10](week10_multicollinearity-judgment/) | - |

## 폴더 구조

`[ ]` 안은 **그 파일을 수정하는 사람**입니다.

```
DAstudy/
├── README.md                     
├── requirements.txt             
├── .github/                      PR·Issue 템플릿, CODEOWNERS
├── data/README.md                데이터 다운로드 방법 (csv는 커밋 xxxx)
├── common/                       [발제자]  공용 코드 — [common] PR, 리뷰 필수
│   ├── load_data.py              # load_bank(), load_home_credit(), load_cookie_cats()
│   ├── bank/preprocess.py        # 4·7주차
│   ├── home_credit/preprocess.py # 5·6·10주차
│   └── evaluate.py               # 7·8주차 (데이터 공통)
├── docs/                         [발제자]  공용 문서 — 모임 후 PR, 리뷰 필수
│   ├── data_dictionary/          # bank.md, home_credit.md, cookie_cats.md
│   ├── decisions.md              # D-번호 뒤에 [bank] / [hc] / [cc] 태그
│   └── audit_checklist.md
├── templates/worksheet.md        
└── weekNN_주제/
    ├── README.md                 [발제자]  교재 범위·개념 정리(모임 전) + 모임 후 해설
    ├── presenter/                [발제자]  발표용 노트북, 도입 데이터 실습, AI 답변 저장 등
    ├── <github-id>/              [전원]    각자 폴더
    │   ├── worksheet.md
    │   ├── analysis.ipynb
    │   └── extra_<데이터명>.ipynb  # 보조 데이터 (선택)
    └── summary.md                [전원]    각자 한 줄씩 **추가만**
```

## 수정하는 방법

**한 PR에 한 종류만**. 
개인 분석 PR에 `common/`·`docs/` 섞이지 않도록 조심해주세요!

### 발제자

| 언제 | PR 제목 | 브랜치 | 수정하는 파일 |
| --- | --- | --- | --- |
| D-7 | (PR 아님) 주차 **Issue** 등록, 리뷰 배정 | — | — |
| D-7 ~ D-2 | `[week03] 발제 준비` | `week03-prep` | `week03_*/README.md`의 교재 범위·개념 정리·발제자 칸<br>`week03_*/presenter/` |
| 스터디 후 | `[week03] 해설 + decisions` | `week03-wrap` | `week03_*/README.md`의 "모임 후 해설"<br>`docs/decisions.md` (D-00N)<br>`docs/audit_checklist.md`<br>`docs/data_dictionary/*.md` (필요할 때) |
| 스터디 후 (해당 주차만) | `[common] 함수명 추가` | `common-<함수명>` | 이번 주 "쌓을 것"에 적힌 `common/` 함수만 |

발표 내용은 노션, 코드·노트북은 `presenter/`에 넣어주세요.

### 피발제자

| PR 제목 | 브랜치 | 수정하는 파일 |
| --- | --- | --- |
| `[week03] 효원 - 결론 한 줄` | `week03-<아이디>` | `week03_*/<아이디>/worksheet.md`, `analysis.ipynb`<br>`week03_*/summary.md`에 한 줄 추가 |
| `[week03-extra] 효원 - 데이터명` (선택) | `week03-<아이디>-extra` | `week03_*/<아이디>/extra_*.ipynb`만 |

- 다른 사람 폴더, `common/`, `docs/`, 주차 README는 건드리지 않기
- 공용 코드 버그나 변수 사전 오류를 찾으면 → Issue로 올리거나 별도 `[common]` PR
- `summary.md`는 여럿이 같은 파일을 고치므로 충돌이 날 수 있음 → 아이디 알파벳 순서 자리에 추가 (4주차 Git 연습)


**`[common]` PR이 있는 주차와 merge 기한**

| 주차 | 함수 | 이 날짜 전까지 merge (다음 사용 주차 D-1) |
| --- | --- | --- |
| 3 | `load_bank()` 확정 | 10.03 (4주차) |
| 4 | `add_prev_contact_flag()` | 11.06 (7주차) |
| 5 | `load_home_credit()`, `fix_days_employed()`, `add_missing_flags()` | **10.31** (5·6주차가 같은 날이라 **모임 전에** 미리) |
| 6 | `cap_outliers()` | 11.21 (10주차) |
| 7 | `make_pipeline()`, `time_split()` | 11.07 (8주차 모임 전) |
| 8 | `report_classification()`, `profit_curve()` | 11.21 (10주차) |
| 9 | `load_cookie_cats()` | **11.14** (9주차 **모임 전에** 미리) |


PR이 merge되면 다음 작업은 `main`을 최신화(`git pull upstream main`)한 뒤 **새 브랜치**에서 시작합니다.

## 처음 세팅

```bash
# 1. GitHub에서 이 레포를 fork 한 뒤
git clone https://github.com/<내-아이디>/DAstudy.git
cd DAstudy
git remote add upstream https://github.com/hyooos/DAstudy.git

# 2. 가상환경 + 패키지
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. 노트북 출력 자동 제거 (커밋할 때 출력이 빠짐)
nbstripout --install

```

노트북에서 공용 코드 불러오기 (`weekNN/<아이디>/analysis.ipynb` 기준):

```python
import sys
sys.path.append("../..")

from common.load_data import load_bank, load_home_credit, load_cookie_cats
from common.bank.preprocess import add_prev_contact_flag
from common.home_credit.preprocess import fix_days_employed

df = load_bank()          # shape까지 확인해 줌
```

## 매주 진행 흐름

| 시점 | 누가 | 할 일 |
| --- | --- | --- |
| D-7 | 발제자 | 주차 Issue 등록, 리뷰 배정 (데이터가 바뀌는 주차는 변수 사전 공유) |
| D-7 ~ D-2 | 발제자 | 주차 폴더 `README.md`(범위, 개념 정리)와 발표 자료 올리기 |
| D-7 ~ D-1 | 전원 | 교재 읽기 |
| D-1 | 전원 | fork 최신화 + 작업 브랜치 생성 (+ 새 데이터 다운로드) |
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
| 공용 코드 | `[common] 함수명 추가/수정` | `[common] fix_days_employed() 추가` |
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
