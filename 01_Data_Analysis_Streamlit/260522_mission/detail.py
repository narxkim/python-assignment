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

if not filtered.empty:
    st.subheader("Target Audience 별 투자 대비 수익률 분석")
    st.divider()
    roi_col1, roi_col2 = st.columns(2)

    st.divider()
    with roi_col1:
        st.markdown("#### 오디언스 X 채널 별 평균 ROI")
        pivot_roi = filtered.pivot_table(
            index="Target_Audience",
            columns="Channel_Used",
            values="ROI",
            aggfunc="mean",
        )
        st.dataframe(pivot_roi.style.format("{:.2f} x"), use_container_width=True)

    #  타겟 오디언스별 전체 평균 ROI 순위 (트리맵)
    with roi_col2:
        st.markdown("#### **타겟 오디언스별 평균 ROI 비중**")

        # 1. 트리맵용 데이터 그룹화 (평균 ROI 계산)
        audience_roi_df = (
            filtered.groupby("Target_Audience", as_index=False)["ROI"]
            .mean()
            .sort_values(by="ROI", ascending=False)
        )

        # 2. Plotly Express 트리맵 생성
        fig_tree_roi = px.treemap(
            audience_roi_df,
            path=["Target_Audience"],  # 분할 기준
            values="ROI",  # 사각형 면적 기준
            color="ROI",  # 색상 그라데이션 기준
            color_continuous_scale="Teal",  # 기존의 Teal 컬러 테마 유지
        )

        # 3. 사각형 내부 텍스트 스타일 커스텀
        # ROI 수치를 '2.45 x' 형태로 명확하게 표시
        fig_tree_roi.update_traces(
            texttemplate="<b>%{label}</b><br>평균 %{value:.2f} x",
            textposition="middle center",  # 에러 방지 및 중앙 정렬
        )

        # 4. 레이아웃 최적화
        fig_tree_roi.update_layout(
            coloraxis_showscale=False,  # 우측 색상바 제거
            margin=dict(l=10, r=10, t=10, b=10),
        )

        # 5. 차트 출력
        st.plotly_chart(fig_tree_roi, use_container_width=True)

    st.divider()

else:
    st.warning("선택한 필터 조건에 맞는 데이터가 없습니다.")
