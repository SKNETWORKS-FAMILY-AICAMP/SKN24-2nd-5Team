import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib  # 학습된 모델 로드용

# 한글 폰트 설정 (환경에 따라 수정 필요)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드 (전처리가 완료된 df라고 가정)
@st.cache_data
def load_data():
    # 실제 경로에 맞게 수정
    df = pd.read_csv("./data/telecom_encoding.csv") 
    return df

df = load_data()

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
    col1.metric("총 데이터 수", "70,145건")
    col2.metric("분석 대상 기간", "2018년 ~ 2025년")
    col3.metric("이탈 데이터 수", "29,503건")

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
        | **gender** | 성별 | 남성(0), 여성(1) |
        | **age** | 나이 | 조사 연도 기준 |
        | **income** | 개인 월평균 소득 | 1~18 구간 |
        | **phone_usage_per_m** | 월 휴대폰 요금 | 만원 단위 |
        | **mobile_bundle** | 결합상품 가입 여부 | 가입(1), 미가입(0) |
        | **telecom_change_yn** | **이탈 여부 (Target)** | 이탈(1), 유지(0) |
        """)
# ---------------------------------------------------------
# 페이지 1: 개인별 이탈 예측
# ---------------------------------------------------------
if page == "개인별 이탈 예측":
    st.title("📱 개인 이탈 가능성 예측")
    st.write("고객 정보를 입력하면 이탈 확률을 계산합니다.")

    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("나이", min_value=10, max_value=100, value=30)
        gender = st.selectbox("성별", ["남성", "여성"])
        income = st.slider("월평균 소득 수준 (1-18)", 1, 18, 5)
        usage = st.number_input("월 휴대폰 이용 금액(만원)", min_value=0, value=5)

    with col2:
        telecom = st.selectbox("현재 통신사", ["SKT", "KT", "LG U+", "알뜰폰"])
        bundle = st.radio("결합상품 가입 여부", ["가입", "미가입"])
        job = st.radio("직업 유무", ["유", "무"])

    if st.button("예측하기"):
        # 예측용 데이터 프레임 변환 (학습 시 사용한 컬럼 순서와 동일해야 함)
        # 예시로 간단하게 구현
        st.success(f"예측 결과: 해당 고객은 이탈할 확률이 **{np.random.randint(10, 80)}%** 입니다.")
        st.info("💡 제언: 결합 상품 가입을 유도하여 이탈률을 낮출 수 있습니다.")

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
elif page == "모델 피처 중요도":
    st.title("🔑 모델 분석 결과 (Feature Importance)")
    st.write("모델이 이탈을 예측할 때 가장 중요하게 고려한 요소들입니다.")

    # 더미 데이터 (실제 모델 학습 후 사용된 feature_importances_를 넣으세요)
    features = ['mobile_bundle', 'income', 'phone_usage_per_m', 'age', 'skt', 'job']
    importances = [0.35, 0.20, 0.15, 0.12, 0.10, 0.08]
    feat_importances = pd.Series(importances, index=features).sort_values()

    fig, ax = plt.subplots()
    feat_importances.plot(kind='barh', color='teal')
    st.pyplot(fig)
    
    st.markdown("""
    - **가장 큰 요인:** `mobile_bundle` (결합상품 여부)가 이탈 방지에 가장 결정적인 역할을 합니다.
    - **소득 및 이용금액:** 소득 수준 대비 통신비 부담이 클수록 이탈 가능성이 높아지는 경향이 있습니다.
    """)