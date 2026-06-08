import streamlit as st
import pandas as pd
import os

# 1. 페이지 레이아웃 넓게
st.set_page_config(layout="wide")


@st.cache_data
def load_marketing():
    # 현재 app.py 파일이 있는 위치를 기준으로 절대 경로를 생성
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "marketing_campaign_dataset.csv")

    # marketing 데이터 불러오기
    df_mk = pd.read_csv(file_path)

    # 전처리 -> $ 및 쉼표 제거 후 실수 타입으로 변환
    df_mk["Acquisition_Cost"] = (
        df_mk["Acquisition_Cost"].str.replace("[$,]", "", regex=True)).astype(float)

    # str -> 날짜 타입으로 변환
    df_mk["Date"] = pd.to_datetime(df_mk["Date"])
    return df_mk


df_mk = load_marketing().copy()

# 사이드바 필터
with st.sidebar:
    st.header("글로벌 필터")
    if st.button("필터 초기화"):
        st.session_state["campaign_types"] = df_mk["Campaign_Type"].unique().tolist()
        st.session_state["location"] = "전체"

    campaign_types = st.multiselect(
        "캠페인 유형",
        df_mk["Campaign_Type"].unique().tolist(),
        default=st.session_state.get(
            "campaign_types", df_mk["Campaign_Type"].unique().tolist()
        ),
        key="campaign_types",
    )
    location = st.selectbox(
        "지역", ["전체"] + sorted(df_mk["Location"].unique().tolist()), key="location"
    )

# 데이터 필터링 후 session_state에 공유
filtered = df_mk[df_mk["Campaign_Type"].isin(campaign_types)]
if location != "전체":
    filtered = filtered[filtered["Location"] == location]

st.session_state["filtered_data"] = filtered


# st.Page + st.navigation
overview = st.Page("overview.py", title="Overview", icon="📊")
detail = st.Page("detail.py", title="Detail", icon="📈")

# 네비게이션 생성
pg = st.navigation([overview, detail])

# 선택된 페이지 실행
pg.run()
