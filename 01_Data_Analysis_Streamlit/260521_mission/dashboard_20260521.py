import streamlit as st ,pandas as pd, plotly.express as px


st.set_page_config(page_title="Dash Board Challenge", page_icon="📊", layout="wide")


# 타이타닉 데이터
@st.cache_data
def load_titanic():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)


# IMDB 데이터
@st.cache_data
def load_imdb():
    im_df = pd.read_csv("./260521_mission/imdb_top_1000.csv")
    im_df["Released_Year"] = pd.to_numeric(im_df["Released_Year"], errors="coerce")
    return im_df

# 타이타닉 대시보드
def titanic_dashboard():
    df = load_titanic().copy()
    df['Age'] = df['Age'].fillna(df['Age'].median())

    st.title('타이타닉 필터 대시보드')

    # 사이드바 위젯 4종
    with st.sidebar:
        st.header("필터")
        st.divider() # 구분선
        pclass_options = st.multiselect("객실 등급", [1,2,3], default=[1,2,3])
        gender = st.selectbox("성별", ["전체", "male", "female"])
        age_range = st.slider("나이 범위", 0, 80, (0,80))
        survived_only = st.checkbox("생존자만 보기")

    filtered = df[df["Pclass"].isin(pclass_options)]
    filtered = filtered[(filtered["Age"] >= age_range[0]) & (filtered["Age"] <= age_range[1])]

    if gender != "전체":
        filtered = filtered[filtered['Sex'] == gender]

    if survived_only:
        filtered = filtered[filtered['Survived'] == 1]

    st.write(f'결과 : {len(filtered)}명')
    st.dataframe(filtered.head(10))

    st.divider()

    # metric 3개
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('필터 선택된 승객', len(filtered))

    with col2:
        st.metric("생존자", filtered["Survived"].sum())

    with col3:
        rate = f"{filtered['Survived'].mean()*100:.1f}%" if len(filtered) > 0 else "N/A" 
        st.metric("생존률", rate)

    st.divider()

    # tab 차트, 데이터로 분리
    tab1, tab2, tab3 = st.tabs(["나이분포 ", "등급별 생존", "데이터"])
    with tab1:
        fig = px.histogram(
            filtered, 
            x='Age', 
            nbins=20, 
            title='나이 분포',
            template='simple_white')
        st.plotly_chart(fig, width='stretch')

    with tab2:
        surv = filtered.groupby("Pclass")["Survived"].mean().reset_index()
        fig2 = px.bar(
            surv, x="Pclass", y="Survived", title="등급별 생존율", template="simple_white",
            labels={"Pclass":"객실 등급", "Survived": '생존율'}
        )
        st.plotly_chart(fig2, width='stretch')
        st.caption('1등급 생존율이 가장 높다.')

    with tab3:
        st.dataframe(
            filtered[["Name", "Survived", "Pclass", "Sex", "Age", "Fare"]], hide_index=True
        )

def imdb_dashboard():

    st.title("IMDB 영화 평점 대시보드")
    imdb = load_imdb().copy()

    with st.sidebar:
        min_rating = st.slider("최소 평점", 7.0, 9.5, 7.6, step=0.1)
        year_range = st.slider("개봉 연도", 1920, 2020, (2000, 2020))

    filtered = imdb[
        (imdb['IMDB_Rating'] >= min_rating) &
        (imdb['Released_Year'] >= year_range[0]) &
        (imdb['Released_Year'] <= year_range[1]) 
    ]

    tab1, tab2 = st.tabs(["평점 분포", "투표 수 vs 평점"])
    # A1. metric 2개 + 평점 히스토그램
    with tab1:
        col1, col2 = st.columns(2)

        col1.metric("영화 수", len(filtered))
        col2.metric("평균 평점", round(filtered['IMDB_Rating'].mean(), 2))

        fig = px.histogram(
            filtered,
            x="IMDB_Rating",
            nbins=20,
            title='평점 분포',
            template="simple_white"
        )
        st.plotly_chart(fig, width='stretch')

    # A2. 투표 수 vs 평점 scatter 탭 추가 (hover_name='Series_Title')
    with tab2:
        fig = px.scatter(
            filtered,
            x="No_of_Votes",
            y="IMDB_Rating",
            hover_name="Series_Title",
            title="투표 수 vs 평점",
            template="simple_white",
            labels={"No_of_Votes":'투표 수', 'IMDB_Rating' : '평점'},
            opacity=0.8
        )
        st.plotly_chart(fig, width='stretch')


with st.sidebar:
    st.title("데이터셋 선택")
    dataset = st.selectbox("", ["Titanic", "IMDB"])
    st.divider()

if dataset == "Titanic":
    titanic_dashboard()
else:
    imdb_dashboard()
