# SKN24-2nd-5Team
# 1. 팀 소개
## 1-1. 팀명
**Girl's night** 🪅
## 1-2. 팀원 소개
|전윤우|류지우|김유진|김수진|권민세|
|---|---|---|---|---|
|  <img width="70%" height="70%" alt="고양" src="https://github.com/user-attachments/assets/dad13c12-cf7d-4766-ba3f-7d6fa9f0affa" />  | <img width="507" height="495" alt="펭" src="https://github.com/user-attachments/assets/21fb66e5-1fb1-4b9c-8dda-cb8a2f994386" /> |  <img width="70%" height="70%" alt="카피" src="https://github.com/user-attachments/assets/ff0e5fb8-f887-451a-b921-d74c0233c424" />  |  <img width="70%" height="70%" alt="강아" src="https://github.com/user-attachments/assets/d754ed6b-2cf0-43cb-90fe-fc0a534344ab" />  |  <img width="50%" height="50%" alt="원숭" src="https://github.com/user-attachments/assets/c1342844-60f4-4489-9831-3db53cf93d9e" />  |
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

## 2-5. 기대 효과

- 데이터 기반 접근을 통한 각 통신사(SKT, KT, LGU+)의 고객 이탈 예측 및 리텐션 전략 수립
- 지속적인 데이터 분석으로 비즈니스적 경쟁력 강화 및 신규 고객 유입 전략 도출
- 고객의 정보 입력 시 이탈 여부 예측 결과 시각화 제공
- 이탈률 감소를 통한 수익성 유지와 마케팅비 효율 향상


# 3. 기술 스택
| 분류 | 기술/도구 |
|---|---|
| 언어 | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| 라이브러리 | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge) ![seaborn](https://img.shields.io/badge/Seaborn-11557c?style=for-the-badge) ![ScikitLearn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| 모델 |![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge) ![LightGBM](https://img.shields.io/badge/LightGBM-00A8E8?style=for-the-badge) ![RandomForest](https://img.shields.io/badge/RandomForest-228B22?style=for-the-badge) ![DecisionTree](https://img.shields.io/badge/DecisionTree-8B4513?style=for-the-badge) |
| 협업 툴 | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-181717?style=for-the-badge&logo=noton&logoColor=white)|
# 4. WBS
<img width="1492" height="707" alt="image" src="https://github.com/user-attachments/assets/348c6656-9d25-4adf-8325-88783acd5ecb" />

# 5. 데이터 전처리 결과서 (EDA)
## 5-1. 데이터 소개
#### 데이터 선정
미디어통계포털의 미디어 패널 조사 자료 중, 2017년부터 2025년까지의 원시 데이터를 사용 <br>


✔️ `pid`를 기준으로 매해 응답자의 구분 가능 <br>
✔️ 조사 대상의 특성을 다양하게 알 수 있는 지표 포함 <br>

<img width="554" height="685" alt="PJ2_EDA" src="https://github.com/user-attachments/assets/773f442b-27dc-4dab-bc52-51dddfdd5cd6" /> <br>
- 출처: [미디어통계포털](https://stat.kisdi.re.kr/kor/contents/ContentsList.html?subject=MICRO10&sub_div=D)

#### 활용 데이터
| column name          | description                                    | data type        |
|----------------------|------------------------------------------------|------------------|
| `id`         | 개인 통합 ID                 | int |
| `gender`        | 성별                     | int  |
| `age`  | 나이(조사한 연도 기준)        | int  |
| `school`  | 최종학력        | int  |
| `mar`    | 결혼 여부                   | int |
| `income`           | 개인 월평균 소득                   | int  |
| `job`       | 직업 유무          | int  |
| `region`      | 지역 구분                             | int |
| `year`  | 조사한 연도        | int  |
| `phone_usage_per_m`              |  월평균 휴대폰 이용 총 금액(천원)                           | int   |
| `mobile_bundle`          | 휴대폰 결합상품 가입 여부           | int |
| `telecom`         | 가입 통신사                       | int   |

---
## 5-2. 데이터 전처리

- 연도별로 분리된 csv 파일 결합
```python
files = glob.glob("../../data/processed/*.csv")

df_list = [pd.read_csv(f) for f in files]
merged_df = pd.concat(df_list, ignore_index=True)

merged_df.to_csv("../../data/processed/merged_telecom.csv", index=False)
```
- 공백으로 수집된 결측치 제거, 10년 이하 응답자 제거
```python
telecom_df = pd.read_csv('../../data/processed/merged_telecom.csv')
telecom_df = telecom_df[(telecom_df != " ").all(axis=1)]
telecom_df_count = telecom_df.groupby('id')['id'].transform('count')
telecom_df = telecom_df[telecom_df_count>=10]
telecom_df.to_csv("../../data/processed/merged_telecom.csv", index=False)
```

### 이탈률 정의
- 작년과 비교하여 올해 통신사가 달라진 경우, 이탈로 간주 (이탈 - 1 / 이탈하지 않음 - 0)
```python
telecom_df['telecom_change'] = telecom_df.groupby('id')['telecom'].shift(1)
telecom_df['telecom_change_yn'] = (telecom_df['telecom_change'] != telecom_df['telecom']).astype(int)

telecom_df['telecom_change'] = telecom_df['telecom_change'].astype('Int64')
telecom_df = telecom_df.drop('telecom_change', axis=1)
```
### mobile_bundle 컬럼 추가
```python
telecom = pd.read_csv('../../data/processed/telecom.csv')
telecom2016 = pd.read_csv('../../data/processed/telecom2016.csv')

telecom2016 = pd.merge(telecom2016, 
                    telecom[['id', 'year', 'mobile_bundle']], 
                    on=['id', 'year'], 
                    how='left')
telecom2016.to_csv("../../data/processed/telecom_f.csv", index=False)
```

### 인코딩
- 범주형 데이터 인코딩 (1, 2 > 0, 1)
```python
telecom_df['gender'] = telecom_df['gender'].replace({1: 0, 2: 1})
telecom_df['job'] = telecom_df['job'].replace({1: 1, 2: 0})
telecom_df['mobile_bundle'] = telecom_df['mobile_bundle'].replace({1: 1, 2: 0})
```
- 범주형 데이터 정규화
```python
telecom_df['school'] = telecom_df['school']-1
telecom_df['income'] = telecom_df['income']-1
```
- 원-핫 인코딩
```python
df_encoded = pd.get_dummies(telecom_df, columns=['mar', 'region', 'telecom'], dtype='int')
telecom_df = telecom_df.rename(columns={
    'region_1': 'seoul',
    'region_2': 'busan',
    'region_3': 'daegu',
    'region_4': 'incheon',
    'region_5': 'gwangju',
    'region_6': 'daejeon',
    'region_7': 'ulsan',
    'region_8': 'gyeonggi',
    'region_9': 'gangwon',
    'region_10': 'chungbuk',
    'region_11': 'chungnam',
    'region_12': 'jeonbuk',
    'region_13': 'jeonnam',
    'region_14': 'gyeongbuk',
    'region_15': 'gyeongnam',
    'region_16': 'jeju',
    'region_17': 'sejong',
    'telecom_1': 'skt',
    'telecom_2': 'kt',
    'telecom_3': 'lgu',
    'telecom_4': 'mvno',
})
```
### 최종 데이터 건수

| 구분   |  건수    |
|---------------|-------------|
| 총 데이터         | 31,572  |
| 유지        | 19,837  |
| 이탈  | 11,735   |
<img width="60%" height="60%" alt="전처리 완료" src="https://github.com/user-attachments/assets/30efcfce-8016-48b3-b2cc-9b0c09a3363b" />

## 5-3. EDA
- 통신사별 이탈 흐름 
> <img width="70%" height="70%" alt="통신사고객흐름도" src="https://github.com/user-attachments/assets/13d6797c-fdfc-47ac-bcff-67c55cd39203" />
> <img width="60%" height="60%" alt="image (1)" src="https://github.com/user-attachments/assets/fecc49ea-e781-4853-a5d6-75828a661034" />
- 결합 상품 유무에 따른 통신사별 이탈률
> <img width="1187" height="690" alt="image" src="https://github.com/user-attachments/assets/c449c7df-c406-4095-a7dd-a7adb2514937" />
> <img width="80%" height="80%" alt="결합상품 유무에 따른 연도별 이탈률" src="https://github.com/user-attachments/assets/2345e93c-64af-4596-ae27-3fc685047fa9" />
- 나이대별 이탈률
> <img width="70%" height="70%" alt="image (2)" src="https://github.com/user-attachments/assets/4bf81513-c5fd-4b08-b08f-709eaf83d3ff" />
- 소득수준별 이탈률
> <img width="70%" height="70%" alt="image (3)" src="https://github.com/user-attachments/assets/a751e0f9-36de-4286-992a-49798991dc5f" />
> <img width="70%" height="70%" alt="image (6)" src="https://github.com/user-attachments/assets/35027cf8-5d3d-48ce-83ab-59daffd07741" />
- 전년 대비 소득 증감에 따른 이탈률
> <img width="60%" height="60%" alt="image (7)" src="https://github.com/user-attachments/assets/f5bba7d4-39c9-481d-8309-dc20f8585ab9" />
- 이탈자들의 직전 2년간의 소득 대비 휴대폰 요금 부담률(평균)
> <img width="561" height="294" alt="image" src="https://github.com/user-attachments/assets/521087af-cf8d-440a-943a-46f208f8963d" />


### 종합 결론
- 통신사의 고객 이탈률은 특정 통신사(SKT) 여부, 결합 상품의 유무, 소득 대비 휴대폰 요금 부담률에 영향을 받음

# 6. 인공지능 학습 결과서
## 6-1. 성능 향상을 위한 시도
- EDA 후 머신러닝을 시도해 보는 과정에서 성능이 생각보다 낮은 문제 발생 → 여러 방법으로 시도
- 하이퍼 파라미터 조정은 모델 학습마다 시도
<img width="70%" height="70%" alt="image" src="https://github.com/user-attachments/assets/21ce43c3-e054-4d80-b617-bdabfd855cbc" />


- XGBoost 임계치 조정
> 조정 O
>
><img width="70%" height="70%" alt="xgboost 임계치 조정" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN24-2nd-5Team/blob/main/image/xgboost%20%EC%9E%84%EA%B3%84%EC%B9%98%20%EC%A1%B0%EC%A0%95.png" />

> 조정 X
>
> <img width="70%" height="70%" alt="xgboost 임계치 조정x" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN24-2nd-5Team/blob/main/image/xgboost%20%EC%9E%84%EA%B3%84%EC%B9%98%20%EC%A1%B0%EC%A0%95x.png" />

### 6-1-1. 데이터 증강
- 기존: 9년치 데이터에 전체 응답한 `id`만 수집/학습
- 전체 데이터 추가
<img width="572" height="130" alt="image" src="https://github.com/user-attachments/assets/2ebf1d20-17bb-4f0b-b8b2-ff485d5473af" />

- 최소 2년 연속 응답자 데이터 추가 (총 데이터 85,288건)
<img width="70%" height="70%" alt="image" src="https://github.com/user-attachments/assets/547e9a25-7170-4c45-b3b2-c17f7b31c2d2" />

> LightGBM 모델 학습 결과
> 
> <img width="60%" height="60%" alt="image" src="https://github.com/user-attachments/assets/c4939175-44ea-48e0-a2d7-a2eb5378bc53" />

- SMOTE로 이탈 데이터 증강
<img width="613" height="223" alt="smote" src="https://github.com/user-attachments/assets/10d9fb85-5ed3-4b24-9f9d-a999138cf8c5" />

### 6-1-2. 이탈률 기준 변경
- 기존: 1년 기준으로 통신사 변동 있을 경우, 이탈로 간주
- 2년 유지 후 통신사 변동 있을 경우, 이탈로 간주
<img width="586" height="311" alt="이탈률 재정의" src="https://github.com/user-attachments/assets/4b53cf97-1475-4763-bbea-ff5ce9305795" />

- 3년 이후 유지 데이터는 표본의 개수가 적어 활용 불가

### 6-1-3. 파생 변수 생성
- 가입기간 변수
<img width="568" height="120" alt="image" src="https://github.com/user-attachments/assets/098af0ed-5523-4aea-94a2-7903d34a19ce" />
<br>

- 소득 대비 휴대폰 요금 부담률
```python
telecom_df['usage_income_ratio'] = (
    telecom_df['phone_usage_per_m'] / (telecom_df['income'] + 1)
)
```
- 직업 기반 소득 안정성
```python
telecom_df['income_if_job'] = (
    telecom_df['job'] * telecom_df['income']
)
```
> 파생 변수 적용 후
> 
> <img width="614" height="230" alt="파생변수=ㅐ" src="https://github.com/user-attachments/assets/6cded041-7bbb-485a-97c0-f4e24a15acaf" />
> <img width="623" height="236" alt="파생변수-x" src="https://github.com/user-attachments/assets/1cfa197e-520a-4077-a441-bcb27f2426a8" />

## 6-2. 최종 모델 선정
<img width="618" height="228" alt="xgboost 파생변수 적용 x" src="https://github.com/user-attachments/assets/9bd040ec-fb78-4bd7-a1f1-698c0e680526" />
<br>

- 약 63%의 정확도
- 이탈 고객(1)을 찾아내는 Recall(재현율)이 0.61로, 실제 이탈자의 약 60% 이상을 찾을 수 있음
- 이전까지의 시도했던 결과들 중에서 가장 안정적인 수치이므로 선정

# 7. 수행결과
## streamlit page
## 주요 기능
✔️ 고객의 이탈 확률 제공 및 고객 분석 결과 제공
✔️ 통신사별 이탈률 데이터 분석 자료 제공

<img width="1919" height="832" alt="메인" src="https://github.com/user-attachments/assets/7b87b806-626b-4871-a7d8-1aec4e0375cc" />
<img width="1919" height="856" alt="칼럼명설명" src="https://github.com/user-attachments/assets/0c9d5047-7b6f-4431-a5c2-d41b9e6786ef" />
<img width="1919" height="841" alt="개인 이탈 고객 가능성 예측 페이지" src="https://github.com/user-attachments/assets/21209f60-432b-4cee-b944-ada57c892b70" />
<img width="1919" height="804" alt="이탈 예측 결과" src="https://github.com/user-attachments/assets/4872cb9f-70fc-4542-8986-9db8539539a6" />
<img width="1915" height="836" alt="분석결과" src="https://github.com/user-attachments/assets/06784e17-9d1d-4752-a658-14e9c9ea94cc" />

# 8. 한계점
- 선정한 데이터가 고객의 이탈 여부에 관한 직접적인 데이터가 아닌 여러 가지 미디어 및 통신에 관련된 설문조사 결과
- 이탈률을 직접 정의하고 필요한 여러 변수들을 직접 고른 탓에 완벽하지 않은 데이터셋이 만들어졌을 수 있다는 가능성
- 다양한 분류 모델을 사용해, 오버샘플링, 하이퍼파라미터 튜닝 등 여러 가지 시도를 했음에도 모델의 성능을 특정 역치 이상으로 올리는 데 어려움 존재

# 9. 한 줄 회고
- 권민세
> 데이터를 직접 뜯어보며 변수 간 상관관계를 분석하고 모델을 만들어가는 과정에서 데이터 분석의 재미를 느낄 수 있었습니다.
> 하지만 이번 프로젝트에서 모델 성능이 기대만큼 향상되지 않아 어려움을 겪었습니다. 하이퍼파라미터 튜닝뿐만 아니라, 성능 개선을 위해 이탈 정의(y)를 수정하고 피처를 재구성하는 등 데이터 수준에서 다양한 시도를 해보았지만 모델 성능은 쉽게 개선되지 않았습니다. 이를 통해 모델 성능은 알고리즘 자체보다도 데이터의 구조와 문제 정의에 더 큰 영향을 받는다는 점을 깨달았습니다.
> 따라서 추후 모델을 설계할 때에는 알고리즘 성능 개선에만 집중하기보다, 데이터 전처리와 feature engineering 단계에서부터 더 체계적으로 접근해야겠다고 생각했습니다.


- 김수진
> 이번 통신사 고객 이탈 예측 프로젝트를 진행하면서, 데이터 정의와 feature 설계가 얼마나 중요한지 깨달았습니다. 처음에는 여러 모델(Logistic Regression, RandomForest, XGBoost, HistGradientBoosting)을 비교하면서 정확도나 F1-score에 집중했지만, 결과를 자세히 살펴보니 모델 성능 차이보다도 threshold 설정과 이탈 기준 정의도 결과에 큰 영향을 준다는 점을 깨달았습니다.


- 김유진
> 지금까지의 프로젝트를 통해 데이터로 말하는 방법을 익히고, 머신러닝 모델 학습을 시키며 다양한 시도를 하고자 하는 생각의 전환을 가지게 되었습니다. 이전 프로젝트에서 아쉬웠던 데이터의 이해도를 쌓기 위해 기획 단계에서부터 팀원들과 소통하며 이야기를 나누었습니다. 아쉬운 점은 이번 조사 데이터가 미디어 관련 설문조사이긴 하지만 막상 EDA와 머신러닝을 진행해 보니 이탈률에 영향을 미칠 만한 데이터는 적었던 것이 제일 아쉬웠습니다. 구하고자 하는 타겟이 다양한 내외부 변수에 의해 달라질 수 있음을 다시 한번 깨달았고, 이후 프로젝트에서는 익숙해진 만큼의 다양한 분석과 시도를 해보고자 합니다.


- 류지우
> 프로젝트를 진행하며 모델 성능에는 피처 설계가 큰 영향을 미친다는 점을 체감했습니다. 전처리를 진행하면서 여러 가지 의미 있는 피처들을 조합하고 파생 변수를 생성하며 어떤 조합이 성능 향상에 효과적인지 탐색하는 과정이 흥미로웠습니다. 또한 하이퍼파라미터와 임계값을 조정하며 성능을 단계적으로 끌어올릴 수 있었고, 이번 경험을 통해 데이터 분석과 전처리 과정이 머신러닝의 핵심이라는 것을 깨달았습니다.


- 전윤우
> 선정한 데이터가 고객 이탈에 관한 테이터가 아닌 단순 설문 데이터였기 때문에, 이탈에 관한 직접적인 정보가 없어 팀원들과 직접 '이탈'을 정의해주어야 했습니다. 그 과정에서 어떤 지점을 '이탈'로 볼 것인지에 대한 고민을 했으며 이 과정에서 필요에 따라 적절한 변수를 정의하는 과정을 배울 수 있었습니다. 팀원들과 심사숙고하며 여러 변수들을 고르고, 전처리에 최선을 다했음에도 여전히 데이터가 완전하지는 못했기에 EDA를 하면서도, 모델을 선정하고 성능 개선 방법론을 적용할 때에도 만족할 만한 결과가 나오지는 않았습니다. 그러나 정제된 데이터가 아닌 진짜 raw data를 활용해서 머신러닝의 파이프라인을 경험할 수 있었다는 점에서 의의가 있었습니다.
