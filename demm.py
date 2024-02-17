import streamlit as st
st.title('Air quality index prediction')

st.write("""
Air quality has always been one of the most important environmental concerns for the general
public and society. Using machine learning algorithms for Air Quality Index (AQI) prediction is helpful
for the analysis of future air quality trends from a macro perspective. When conventionally using a single
machine learning model to predict air quality, it is challenging to achieve a good prediction outcome under
various AQI fluctuation trends.
""")

st.button("PREDICT", type="primary")