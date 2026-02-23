# SKN24-2nd-5Team
# 1. 팀 소개
## 1-1. 팀명
**Girl's night** 🪅
## 1-2. 팀원 소개
|전윤우|류지우|김유진|김수진|권민세|
|----|---|---|---|---|
| 이미지 | 이미지 | 이미지 | 이미지 | 이미지 |
| [Yunu-Jeon](https://github.com/Yunu-Jeon) | [jia11234](https://github.com/jia11234) | [youjin](https://github.com/shortcut-2) | [Sujin Kim](https://github.com/KimSujin02) | [KweonMinSe0109](https://github.com/KweonMinSe0109) |
# 2. 프로젝트 개요
## 2-1. 프로젝트 명
**국내 통신사 고객 이탈률 예측 모델 및 예측 서비스 제공**
## 2-2. 프로젝트 소개
본 프로젝트는 국내 통신사 고객 데이터를 기반으로 개인 특성과 통신사 이용 관련 정보를 분석하여 **고객 이탈률(Churn)** 을 예측하고자 한다. 다양한 고객 특성과 환경 요인을 분석하여 이탈률과의 관계를 파악하고, 이를 바탕으로 이탈 위험 고객을 조기에 식별하며 주요 영향 요인을 도출하는 것을 목표로 한다.
## 2-3. 프로젝트 배경

> 국내 이동통신 시장은 5G 서비스 경쟁 우위 확보를 위한 치열한 주파수 경쟁, 결합상품 중심의 경쟁, 자급제 단말 이용 증대에 따른 단말 제조사와 오픈마켓의 영향력 확대, MVNO 가입자 급성장, 통신시장의 플레이그라운드 및 참여자 확대 등으로 경쟁이 복잡해지고 심화되고 있다.
> 
> *-유지은 외, "최근 국내 이동통신서비스 이용행태 분석" 전자통신동향분석 제37권 제3호, 2022년 6월*

<br>

이동통신 사업은 가입자 기반이 확대될수록 요금 수익이 발생하는 구조로, 초기 유치 비용을 감수하더라도 **가입자를 확보하는 것** 이 장기 수익성에 중요한 요소로 작용한다. 즉, 통신사의 고객 유치를 위한 마케팅비는 단순한 판촉 비용을 넘어 가입자 확보와 시장 점유율을 좌우하는 핵심 투자 지표로써 활용된다.


<img width="914" height="321" alt="image" src="https://github.com/user-attachments/assets/ba8295ab-409e-4c47-b27c-ab8fcc7e364a" />

[통신3사, 지난해 가입자 유치전쟁에 마케팅비 6% 증가 - 디지털타임스, 이혜선 기자](https://www.dt.co.kr/article/12046646?ref=naver)

그러나 영업이익에 영향을 끼치는 마케팅비의 활용은 이동통신 사업자의 입장에서 줄이면 신규 고객 유치에 난항을 겪고, 늘리면 영업이익이 줄어드는 딜레마에 빠질 수밖에 없다.

## 2-4. 프로젝트 목표

**① 주요 영향 요인 분석:** 고객 이탈에 영향을 미치는 핵심 변수들을 식별하고 그 중요도를 정량적으로 분석 <br>

**② 이탈 예측 모델 개발:** 다양한 머신러닝 분류 모델을 활용하여 통신사 고객의 이탈 가능성을 예측하는 최적의 모델을 도출 <br>

**③ 기업 의사결정 지원:** 예측 결과를 기반으로 고객 유지 전략 수립 및 마케팅 효율화를 위한 데이터 기반 인사이트를 제공 <br>


> **"통신사 고객의 이탈은 요금 수준, 결합상품 이용 여부, 통신사 변경 이력, 인구통계학적 특성 등의 복합적 요인에 의해 발생하며, 이러한 변수들의 상호작용을 통해 예측이 가능하다."**


이 가설을 바탕으로 실제 패널 데이터를 정제·분석한 뒤 머신러닝 분류 모델을 구축하여 이탈에 영향을 미치는 주요 요인을 도출하고, 예측 성능을 검증하고자 한다.
# 3. 기술 스택
| 분류 | 기술/도구 |
|---|---|
| 언어 | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| 라이브러리 | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge) ![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge) <br> ![GradientBoosting](https://img.shields.io/badge/GradientBoosting-00A8E8?style=for-the-badge) ![RandomForest](https://img.shields.io/badge/RandomForest-228B22?style=for-the-badge) ![DecisionTree](https://img.shields.io/badge/DecisionTree-8B4513?style=for-the-badge) ![ScikitLearn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| 협업 툴 | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) |
# 4. WBS
# 5. 데이터 전처리 결과서 (EDA)
## 5-1. 데이터 개요
### 데이터 선정
미디어통계포털의 미디어 패널 조사 자료 중, 2017년부터 2025년까지의 원시 데이터를 사용 <br>


✔️ `pid`를 기준으로 매해 응답자의 구분 가능 <br>
✔️ 조사 대상의 특성을 다양하게 알 수 있는 지표 포함 <br>

<img width="554" height="685" alt="PJ2_EDA" src="https://github.com/user-attachments/assets/773f442b-27dc-4dab-bc52-51dddfdd5cd6" /> <br>
- 출처: [미디어통계포털](https://stat.kisdi.re.kr/kor/contents/ContentsList.html?subject=MICRO10&sub_div=D)

#### 활용 데이터 (원본 기준)
| column name          | description                                    | data type        |
|----------------------|------------------------------------------------|------------------|
| `pid`         | 개인 통합 ID                 | int |
| `gender`        | 성별                     | int  |
| `byear`  | 출생연도        | int  |
| `mar`    | 결혼 여부                   | int |
| `income`           | 개인 월평균 소득                   | int  |
| `job1`       | 직업 유무          | int  |
| `area`      | 지역 구분                             | int |
| `c01002`              |  월평균 휴대폰 이용 총 금액(만원)                           | int   |
| `c02003`          | 휴대폰 결합상품 가입 여부           | int |
| `a03008`         | 스마트폰 가입 이동 통신사                       | int   |
### 데이터 확인



# 6. 인공지능 학습 결과서
# 7. 수행결과
# 8. 한계점 
# 9. 한 줄 회고
