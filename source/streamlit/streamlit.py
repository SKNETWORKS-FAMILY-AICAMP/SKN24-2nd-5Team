from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  
import joblib
from xgboost import XGBClassifier  # 학습된 모델 로드용

# 한글 폰트 설정 (환경에 따라 수정 필요)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
st.set_page_config(layout="wide")

# 데이터 로드 (전처리가 완료된 df라고 가정)
@st.cache_data
def load_data():
    # 실제 경로에 맞게 수정
    df = pd.read_csv("../../data/processed/telecom_encoding.csv") 
    return df

df = load_data()

@st.cache_resource
def train_model():
    # 데이터 로드 및 학습 (실제 서비스에서는 학습된 모델 .pkl 파일을 불러오는 것이 좋습니다)
    df = pd.read_csv('../../data/processed/telecom_encoding.csv')
    
    # 모델 학습 시 제외했던 컬럼들 동일하게 적용
    X = df.drop(['telecom_change_yn', 'mar_1', 'mar_2', 'mar_3', 'mar_4', 'gender'], axis=1)
    y = df['telecom_change_yn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=24)
    
    # 제공해주신 최적 파라미터 적용
    xgb_clf = XGBClassifier(
        n_estimators=1000, learning_rate=0.03, max_depth=7,
        min_child_weight=3, scale_pos_weight=1.37, subsample=0.8,
        colsample_bytree=0.8, random_state=42, eval_metric='logloss'
    )
    xgb_clf.fit(X_train, y_train)
    return xgb_clf, X.columns
# 모델과 컬럼 리스트 준비
model, model_columns = train_model()

# @st.cache_resource
# def load_trained_model():
#     # 저장된 모델 파일 불러오기
#     model = joblib.load('xgb_model.pkl')
#     # 저장된 컬럼 리스트 불러오기
#     columns = joblib.load('model_columns.pkl')
#     return model, columns

# # 모델 로드
# try:
#     model, model_columns = load_trained_model()
# except FileNotFoundError:
#     st.error("모델 파일(xgb_model.pkl)을 찾을 수 없습니다. 경로를 확인해주세요.")
#     st.stop()

# 사이드바 메뉴
st.sidebar.title("통신사 이탈 분석 서비스")
page = st.sidebar.radio("메뉴 선택", ["프로젝트 개요", "개인별 이탈 예측", "통신사별 이탈률 분석", "모델 피처 중요도"])

# ---------------------------------------------------------
# 페이지 0: 프로젝트 개요 (Overview)
# ---------------------------------------------------------
if page == "프로젝트 개요":
    st.title("🚀 국내 통신사 고객 이탈 예측 프로젝트")
    st.subheader("Girl's night 🪅")
    
    # 프로젝트 소개
    st.markdown("### 1. 프로젝트 배경")
    st.info("""
    국내 이동통신 시장은 5G 경쟁, 결합상품 중심의 마케팅, 알뜰폰(MVNO)의 급성장 등으로 인해 
    고객 유치 경쟁이 매우 심화된 상태입니다. 
    가입자를 확보하고 유지하는 것은 통신사의 장기 수익성을 결정짓는 핵심 투자 지표입니다.
    """)
    
    # 주요 지표 (이미지 대신 메트릭으로 표현 가능)
    col1, col2, col3 = st.columns(3)
    col1.metric("총 데이터 수", "31,572건")
    col2.metric("분석 대상 기간", "2017년 ~ 2025년")
    col3.metric("이탈 데이터 수", "11,735건")

    # 프로젝트 목표
    st.markdown("---")
    st.markdown("### 2. 프로젝트 목표")
    st.markdown("""
    * **주요 영향 요인 분석:** 고객 이탈에 영향을 미치는 핵심 변수 식별
    * **이탈 예측 모델 개발:** 머신러닝을 활용한 최적의 예측 성능 도출
    * **기업 의사결정 지원:** 데이터 기반의 마케팅 전략 및 리텐션 전략 수립 지원
    """)

    # 분석 가설
    st.success("""
    **핵심 가설:** "통신사 고객의 이탈은 요금 수준, 결합상품 이용 여부, 통신사 변경 이력, 인구통계학적 특성 등의 복합적 요인에 의해 발생하며, 이를 통해 예측이 가능하다."
    """)

    # 데이터 구조 소개
    with st.expander("📊 활용 데이터 컬럼 상세 보기"):
        st.write("""
        | 컬럼명 | 설명 | 비고 |
        | :--- | :--- | :--- |
        | **id** | 개인 통합 ID | 고유 식별 번호 |
        | **gender** | 성별 | 남성(0), 여성(1) |
        | **age** | 나이 | 조사 연도 기준 |
        | **school** | 최종 학력 | 1~6 구간 |
        | **mar** | 결혼 여부 | 원-핫 인코딩 (mar_1~4) |
        | **income** | 개인 월평균 소득 | 1~18 구간 |
        | **job** | 직업 유무 | 유(1), 무(0) |
        | **region** | 거주 지역 | 17개 시도 원-핫 인코딩 |
        | **year** | 조사한 연도 | 2018 ~ 2025 |
        | **phone_usage_per_m** | 월평균 휴대폰 이용 요금 | 만원 단위 |
        | **mobile_bundle** | 휴대폰 결합상품 가입 여부 | 가입(1), 미가입(0) |
        | **telecom** | 가입 통신사 | 원-핫 인코딩 (skt, kt, lgu, mvno) |
        | **telecom_change_yn** | **이탈 여부 (Target)** | 유지(0), 이탈(1) |
        """)
# ---------------------------------------------------------
# 페이지 1: 개인별 이탈 예측
# ---------------------------------------------------------
if page == "개인별 이탈 예측":
    st.title("📱 개인 고객 이탈 가능성 예측")
    st.write("고객의 정보를 입력하면 XGBoost 모델이 실시간으로 이탈 확률을 계산합니다.")
    # 1. 사이드바나 메인 화면에 가이드 추가
    with st.expander("💰 소득 수준 가이드 확인하기"):
        st.write("""
        - 1	   : 소득 없음
        - 2	   : 50만 원 미만
        - 3	   : 500100만 원 미만
        - 4	   : 1000150만 원 미만
        - 5	   : 1500200만 원 미만
        - 6	   : 2000250만 원 미만
        - 7	   : 2500300만 원 미만
        - 8	   : 3000350만 원 미만
        - 9	   : 3500400만 원 미만
        - 10   : 4000450만 원 미만
        - 11   : 4500500만 원 미만
        - 12   : 5000550만 원 미만
        - 13   : 5500600만 원 미만
        - 14   : 6000650만 원 미만
        - 15   : 6500700만 원 미만
        - 16   : 7000750만 원 미만
        - 17   : 7500800만 원 미만
        - 18   : 800만 원 이상
        """)
    with st.expander("📕 학력 수준 가이드 확인하기"):
        st.write("""
        - 1	: 미취학
        - 2	: 초졸 이하
        - 3	: 중졸 이하
        - 4	: 고졸 이하
        - 5	: 대졸 이하
        - 6	: 대학원 재학 이상
        """)

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("인적 사항")
            age = st.number_input("나이", 10, 100, 30)
            school = st.slider("학력 (1-6)", 1, 6, 3)
            # 결혼 여부 셀렉트박스 추가
            mar_status = st.selectbox("결혼 여부", ["미혼", "기혼", "사별", "이혼"])
            job = st.radio("직업 유무", ["유 (1)", "무 (0)"], index=0)
            
        with col2:
            st.subheader("통신 이용 행태")
            telecom = st.selectbox("현재 통신사", ["SKT", "KT", "LG U+", "MVNO"])
            usage = st.number_input("월평균 요금 (만원)", 0, 100, 5)
            bundle = st.radio("결합상품 가입", ["가입 (1)", "미가입 (0)"], index=0)
            
        with col3:
            st.subheader("경제 지표")
            income = st.slider("월평균 소득 수준 (1-18)", 1, 18, 5)
            year = st.selectbox("기준 연도", [2024, 2025])
            # 지역 정보는 데이터가 많으므로 서울을 기본값으로 설정
            region = st.selectbox("거주 지역", ["seoul", "busan", "daegu", "incheon", "gwangju", "daejeon", "ulsan", "gyeonggi", "gangwon", "chungbuk", "chungnam", "jeonbuk", "jeonnam", "gyeongbuk", "gyeongnam", "jeju", "sejong"])

        submit = st.form_submit_button("이탈 여부 예측하기")

    if submit:
        # 1. 입력 데이터를 모델용 데이터프레임으로 변환
        input_data = pd.DataFrame(columns=model_columns)
        input_data.loc[0] = 0  # 모든 값을 0으로 초기화
        
        # 2. 기본 수치 입력
        input_data['age'] = age
        input_data['year'] = year
        input_data['school'] = school
        input_data['income'] = income
        input_data['phone_usage_per_m'] = usage
        input_data['job'] = 1 if "유" in job else 0
        input_data['mobile_bundle'] = 1 if "가입" in bundle else 0
        input_data['id'] = 99999  # 임의의 ID 값
        
        # 3-1. 결혼 여부 원-핫 매핑 추가
        mar_mapping = {"미혼": "mar_1", "기혼": "mar_2", "사별": "mar_3", "이혼": "mar_4"}
        input_data[mar_mapping[mar_status]] = 1
        
        # 3-2. 원-핫 인코딩 수동 매핑 (지역 및 통신사)
        input_data[region] = 1
        input_data[telecom.lower().replace(" ", "").replace("+", "")] = 1 # 'lgu', 'skt' 등 매핑
        
        # 4. 예측 수행
        # 컬럼 순서를 학습 모델과 동일하게 맞춤
        input_data = input_data[model_columns]
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        # 5. 결과 출력
        st.markdown("---")
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            if prediction == 1:
                st.error(f"### 예측 결과: **이탈 위험** ⚠️")
            else:
                st.success(f"### 예측 결과: **유지 가능성 높음** ✅")
        
        with res_col2:
            st.metric("이탈 확률", f"{probability*100:.2f}%")
            st.progress(float(probability))

        st.info(f"💡 분석 결과: 이 고객은 현재 `{telecom}` 이용 중이며, 결합상품 `{bundle}` 상태입니다. 요금 부담 및 소득 수준을 고려할 때 { '주의가 필요합니다.' if probability > 0.5 else '안정적인 상태입니다.' }")
# ---------------------------------------------------------
# 페이지 2: 통신사별 이탈률 분석 (질문하신 원-핫 처리 포함)
# ---------------------------------------------------------
elif page == "통신사별 이탈률 분석":
    st.title("📊 통신사별 데이터 분석")

    # 원-핫 인코딩된 통신사를 하나로 합쳐서 시각화
    carrier_cols = ['skt', 'kt', 'lgu', 'mvno']
    df['telecom_label'] = df[carrier_cols].idxmax(axis=1).map({
        'skt': 'SKT', 'kt': 'KT', 'lgu': 'LG U+', 'mvno': '알뜰폰 서비스'
    })

    # 그래프 1: 통신사별 이탈률
    st.subheader("1. 통신사별 평균 이탈률")
    telecom_churn = df.groupby("telecom_label")["telecom_change_yn"].mean().sort_values()
    
    fig, ax = plt.subplots()
    telecom_churn.plot(kind="bar", ax=ax, color='skyblue')
    ax.set_ylabel("이탈률")
    st.pyplot(fig)

    # 그래프 2: 결합상품 유무에 따른 이탈률 (상관계수 기반 추천 분석)
    st.subheader("2. 결합상품 가입 여부에 따른 이탈률 비교")
    bundle_churn = df.groupby(["telecom_label", "mobile_bundle"])["telecom_change_yn"].mean().unstack()
    bundle_churn.columns = ['미가입', '가입']
    
    fig2, ax2 = plt.subplots()
    bundle_churn.plot(kind="bar", ax=ax2)
    st.pyplot(fig2)
# ---------------------------------------------------------
# 페이지 3: 피처 중요도
# ---------------------------------------------------------
# 피처 중요도 페이지도 실제 모델 기반으로 자동 업데이트 되도록 수정
elif page == "모델 피처 중요도":
    st.title("🔑 XGBoost 피처 중요도 (Feature Importance)")
    feat_impt_ser = pd.Series(model.feature_importances_, index=model_columns).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    feat_impt_ser.tail(15).plot(kind='barh', ax=ax, color='orange')
    ax.set_title("상위 15개 핵심 변수")
    st.pyplot(fig)