pip install pandas

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 타이타닉 데이터 불러오기
titanic_data = pd.read_csv('/content/titanic.csv')  # 데이터셋의 실제 경로로 수정하세요.

# 상관 계수 계산
correlation_matrix = titanic_data.corr()

# Streamlit 앱
st.title('타이타닉 데이터셋 - 상관 관계 분석')

# 상관 계수 표시
st.write('### 상관 계수 행렬:')
st.write(correlation_matrix)

# Plotly Express를 사용하여 히트맵 그리기
fig = px.imshow(correlation_matrix,
                labels=dict(x='변수', y='변수', color='상관 관계'),
                x=correlation_matrix.columns,
                y=correlation_matrix.columns,
                color_continuous_scale='coolwarm',
                zmin=-1, zmax=1)

# 레이아웃을 업데이트하여 가독성 향상
fig.update_layout(width=800, height=600, title='상관 관계 히트맵', xaxis_showgrid=False, yaxis_showgrid=False)

# Plotly 차트 표시
st.write('### 상관 관계 히트맵:')
st.plotly_chart(fig)

# 원래의 seaborn 히트맵 표시 (선택 사항)
st.write('### 원본 Seaborn 히트맵:')
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('데이터 변수 간 상관 관계')
st.pyplot()

# Streamlit 앱 실행: streamlit run 파일명.py
