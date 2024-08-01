import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Streamlit 웹앱 제목 및 설명
st.title("🔵 포물선 운동 시뮬레이터")
st.markdown("물체의 질량, 초기 속력, 발사 각도를 입력하고 포물선 운동을 시뮬레이션합니다.")

# 사용자 입력 받기
mass = st.number_input("물체의 질량 (kg):", min_value=0.1, max_value=100.0, value=1.0, step=0.1)
initial_velocity = st.number_input("물체의 초기 속력 (m/s):", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
launch_angle = st.number_input("발사 각도 (도):", min_value=0, max_value=90, value=45, step=1)

# 입력 받은 값을 바탕으로 시뮬레이션
if st.button("시뮬레이션 시작"):
    # 초기 조건 설정
    theta = np.radians(launch_angle)
    v0x = initial_velocity * np.cos(theta)
    v0y = initial_velocity * np.sin(theta)
    g = 9.8  # 중력 가속도

    # 최고 지점의 높이 (최고점에서의 y)
    max_height = (v0y**2) / (2 * g)

    # 지면 도달 시간 (전체 비행 시간)
    time_of_flight = (2 * v0y) / g

    # 지면 도달 거리 (수평 거리)
    range_distance = v0x * time_of_flight

    # 시간 배열
    t = np.linspace(0, time_of_flight, num=500)

    # 포물선 운동 방정식
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2

    # Plotly 그래프 생성
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='포물선 궤적',
                                    line=dict(width=4)))  # 라인 굵기 설정
    fig.update_layout(title="포물선 운동 궤적",
                      xaxis_title="거리 (m)",
                      yaxis_title="높이 (m)",
                      yaxis=dict(scaleanchor="x", scaleratio=1))

    st.plotly_chart(fig)

    # 결과 표시 (글씨 크기 크게 설정)
    st.markdown(f"<div style='font-size: 24px;'><strong>최고 지점의 높이:</strong> {max_height:.2f} m</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 24px;'><strong>지면 도달 시간:</strong> {time_of_flight:.2f} s</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 24px;'><strong>지면 도달 거리:</strong> {range_distance:.2f} m</div>", unsafe_allow_html=True)
