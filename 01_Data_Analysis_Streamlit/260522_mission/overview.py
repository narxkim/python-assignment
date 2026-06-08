import streamlit as st
import plotly.express as px

st.title("Marketing Campaign Dashboard")
st.divider()
st.markdown("<br>", unsafe_allow_html=True)

# app.py에서 공유한 필터 데이터 가져오기
if "filtered_data" in st.session_state:
    filtered = st.session_state["filtered_data"]
else:
    st.warning("데이터를 불러올 수 없습니다. 메인 홈을 확인해 주세요.")
    st.stop()

# 주요 성과 지표(KPI)
st.subheader("주요 성과 지표(KPI)")
col1, col2, col3 = st.columns(3)

if not filtered.empty:
    avg_roi = filtered["ROI"].mean()
    total_clicks = filtered["Clicks"].sum()
    avg_conversion = filtered["Conversion_Rate"].mean() * 100

    col1.metric("평균 ROI", f"{avg_roi:.2f} x")
    col2.metric("총 클릭 수 (Clicks)", f"{total_clicks: ,}회")
    col3.metric("평균 전환율 (Conversion)", f"{avg_conversion:.2f} %")

    st.divider()

    # 타겟 오디언스별 선호 채널 분석
    st.subheader("Target Audience 별 선호 채널 분석 (유입 기준)")
    st.divider()
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("#### **오디언스 X 채널 별 총 클릭 수**")
        pivot_clicks = filtered.pivot_table(
            index="Target_Audience",
            columns="Channel_Used",
            values="Clicks",
            aggfunc="sum",
        )
        st.dataframe(pivot_clicks.style.format("{:,.0f}"), use_container_width=True)

    # 💡 에러 보정 및 레이아웃 최적화 완료된 트리맵 영역
    with chart_col2:
        st.markdown("#### **타겟 오디언스별 총 클릭 수 비중**")

        # 1. 트리맵용 데이터 그룹화 수집
        audience_clicks_mk_df = (
            filtered.groupby("Target_Audience", as_index=False)["Clicks"]
            .sum()
            .sort_values(by="Clicks", ascending=False)
        )

        # 2. 사각형 내부에 표기할 각 그룹별 '전체 대비 비율(%)' 계산
        total_clicks_sum = audience_clicks_mk_df["Clicks"].sum()
        audience_clicks_mk_df["Percentage"] = (
            audience_clicks_mk_df["Clicks"] / total_clicks_sum
        ) * 100

        # 3. Plotly Express 트리맵 생성
        fig_tree = px.treemap(
            audience_clicks_mk_df,
            path=["Target_Audience"],  # 분할할 그룹 기준
            values="Clicks",  # 사각형 면적 결정 기준
            color="Clicks",  # 그라데이션 색상 기준
            color_continuous_scale="Blues",
        )

        # 4. textposition을 'middle center'로 수정하여 에러 원천 차단
        fig_tree.update_traces(
            texttemplate="<b>%{label}</b><br>%{value:,.0f}회<br>(%{customdata[0]:.1f}%)",
            customdata=audience_clicks_mk_df[["Percentage"]],
            textposition="middle center",  #'inside' 대신 트리맵 규격에 맞는 고정값 사용
        )

        # 5. 불필요한 레이아웃 제거 및 마진 조정
        fig_tree.update_layout(
            coloraxis_showscale=False, margin=dict(l=10, r=10, t=10, b=10)
        )

        # 6. 스트림릿 화면에 차트 출력
        st.plotly_chart(fig_tree, use_container_width=True)
else:
    st.warning("선택한 필터 조건에 맞는 데이터가 없습니다.")
