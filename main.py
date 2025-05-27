import streamlit as st
import plotly.express as px

st.set_page_config(page_title="챔피언스 리그 우승 분석", layout="wide")

st.title("🏆 최근 25년간 챔피언스 리그 우승 팀 분석 (1999–2024)")

# 우승 데이터
winners = {
    "레알 마드리드": 8,
    "바르셀로나": 4,
    "바이에른 뮌헨": 3,
    "AC 밀란": 2,
    "리버풀": 2,
    "첼시": 2,
    "맨체스터 유나이티드": 2,
    "맨체스터 시티": 1,
    "인터 밀란": 1,
    "포르투": 1,
}

# Plotly 시각화
fig = px.bar(
    x=list(winners.keys()),
    y=list(winners.values()),
    labels={'x': '클럽', 'y': '우승 횟수'},
    title='클럽별 UEFA 챔피언스 리그 우승 횟수 (1999–2024)',
    text=list(winners.values())
)

fig.update_traces(marker_color='crimson', textposition='outside')
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)

# 참고 정보
st.markdown("""
#### 📌 주요 정보
- 데이터 범위: **1999–2000 시즌 ~ 2023–24 시즌**
- 🥇 **레알 마드리드**: 8회 우승
- 🔍 최신 우승팀 (2024): 레알 마드리드 vs 도르트문트 승리
""")
