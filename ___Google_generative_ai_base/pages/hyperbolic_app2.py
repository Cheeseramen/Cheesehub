import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Streamlit 웹앱 제목 및 설명
st.title("🔵 포물선 운동 시뮬레이터")
st.markdown("두 개의 물체에 대해 질량, 초기 속력, 발사 각도를 입력하고 포물선 운동을 시뮬레이션합니다.")

# 물체 1의 사용자 입력 받기
st.header("물체 1")
mass1 = st.number_input("물체 1의 질량 (kg):", min_value=0.1, max_value=100.0, value=1.0, step=0.1)
initial_velocity1 = st.number_input("물체 1의 초기 속력 (m/s):", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
launch_angle1 = st.number_input("물체 1의 발사 각도 (도):", min_value=0, max_value=90, value=45, step=1)

# 물체 2의 사용자 입력 받기
st.header("물체 2")
mass2 = st.number_input("물체 2의 질량 (kg):", min_value=0.1, max_value=100.0, value=1.0, step=0.1)
initial_velocity2 = st.number_input("물체 2의 초기 속력 (m/s):", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
launch_angle2 = st.number_input("물체 2의 발사 각도 (도):", min_value=0, max_value=90, value=45, step=1)

# 입력 받은 값을 바탕으로 시뮬레이션
if st.button("시뮬레이션 시작"):
    # 중력 가속도
    g = 9.8

    # 물체 1의 계산
    theta1 = np.radians(launch_angle1)
    v0x1 = initial_velocity1 * np.cos(theta1)
    v0y1 = initial_velocity1 * np.sin(theta1)
    max_height1 = (v0y1**2) / (2 * g)
    time_of_flight1 = (2 * v0y1) / g
    range_distance1 = v0x1 * time_of_flight1
    t1 = np.linspace(0, time_of_flight1, num=500)
    x1 = v0x1 * t1
    y1 = v0y1 * t1 - 0.5 * g * t1**2

    # 물체 2의 계산
    theta2 = np.radians(launch_angle2)
    v0x2 = initial_velocity2 * np.cos(theta2)
    v0y2 = initial_velocity2 * np.sin(theta2)
    max_height2 = (v0y2**2) / (2 * g)
    time_of_flight2 = (2 * v0y2) / g
    range_distance2 = v0x2 * time_of_flight2
    t2 = np.linspace(0, time_of_flight2, num=500)
    x2 = v0x2 * t2
    y2 = v0y2 * t2 - 0.5 * g * t2**2

    # Plotly 그래프 생성
    fig = go.Figure()

    # 물체 1의 궤적 추가
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='물체 1 궤적',
                             line=dict(width=4, color='blue')))

    # 물체 2의 궤적 추가
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='물체 2 궤적',
                             line=dict(width=4, color='red')))

    # 그래프 레이아웃 설정
    fig.update_layout(title="포물선 운동 궤적",
                      xaxis_title="거리 (m)",
                      yaxis_title="높이 (m)",
                      yaxis=dict(scaleanchor="x", scaleratio=1))

    st.plotly_chart(fig)

    # 물체 1과 물체 2의 결과 표시 (같은 줄에, 구분선 포함)
    st.markdown("""
    <style>
    .result-table {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .result-box {
        width: 45%;
    }
    .separator {
        width: 5%;
        text-align: center;
        font-size: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-table">
        <div class="result-box">
            <h3>물체 1 결과</h3>
            <div style='font-size: 24px;'><strong>최고 지점의 높이:</strong> {max_height1:.2f} m</div>
            <div style='font-size: 24px;'><strong>지면 도달 시간:</strong> {time_of_flight1:.2f} s</div>
            <div style='font-size: 24px;'><strong>지면 도달 거리:</strong> {range_distance1:.2f} m</div>
        </div>
        <div class="separator">|</div>
        <div class="result-box">
            <h3>물체 2 결과</h3>
            <div style='font-size: 24px;'><strong>최고 지점의 높이:</strong> {max_height2:.2f} m</div>
            <div style='font-size: 24px;'><strong>지면 도달 시간:</strong> {time_of_flight2:.2f} s</div>
            <div style='font-size: 24px;'><strong>지면 도달 거리:</strong> {range_distance2:.2f} m</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
