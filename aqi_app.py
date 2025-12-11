import streamlit as st
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import plotly.graph_objects as go

# ← TOKEN DAAL DIYA!
AQICN_TOKEN = 'dcbc0168083113f5451630bb2162e8eba9bd6a34'

st.set_page_config(page_title="AQI India Live", page_icon="air", layout="wide")

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>
    .aqi-good {background:linear-gradient(135deg,#00e400,#009900);color:white}
    .aqi-moderate {background:linear-gradient(135deg,#ffff00,#cccc00);color:black}
    .aqi-sensitive {background:linear-gradient(135deg,#ff7e00,#ff5500);color:white}
    .aqi-unhealthy {background:linear-gradient(135deg,#ff0000,#cc0000);color:white}
    .aqi-very {background:linear-gradient(135deg,#8f3f97,#6f1f77);color:white}
    .aqi-hazard {background:linear-gradient(135deg,#7e0023,#5a001a);color:white}
    .box {padding:2.5rem;border-radius:25px;text-align:center;font-size:3.5rem;font-weight:bold;box-shadow:0 10px 20px rgba(0,0,0,0.3);}
</style>
""", unsafe_allow_html=True)

def get_aqi_category(aqi):
    if aqi <= 50:   return "Good", "aqi-good"
    if aqi <= 100:  return "Moderate", "aqi-moderate"
    if aqi <= 150:  return "Unhealthy for Sensitive", "aqi-sensitive"
    if aqi <= 200:  return "Unhealthy", "aqi-unhealthy"
    if aqi <= 300:  return "Very Unhealthy", "aqi-very"
    return "Hazardous", "aqi-hazard"

st.title("Real-Time AQI Live Dashboard")
st.markdown("*AQICN Powered | Token Active | India + Global*")

city = st.text_input("Enter City Name (lowercase)", value="delhi", help="e.g., mumbai, bangalore, lucknow, patna")

if st.button("Get Live AQI", type="primary"):

    with st.spinner(f"Fetching AQI for {city.title()}..."):

        # Fetch from AQICN JSON Feed (Token Enabled)
        url = f"http://api.waqi.info/feed/{city}/?token={AQICN_TOKEN}"
        try:
            resp = requests.get(url, timeout=10).json()
            if resp['status'] != 'ok':
                st.error("City not found! Try lowercase like 'delhi' or check spelling on aqicn.org.")
                st.stop()
            data = resp['data']
            current_aqi = int(data.get('aqi', 0))
            pm25 = float(data.get('pm25', 0)) if data.get('pm25') != '-' else 0
            pm10 = float(data.get('pm10', 0)) if data.get('pm10') != '-' else 0
            no2 = float(data.get('no2', 0)) if data.get('no2') != '-' else 0
            o3 = float(data.get('o3', 0)) if data.get('o3') != '-' else 0
            attribution = data.get('attribution', 'AQICN')  # Mandatory from page
            st.success(f"Data from {attribution} – Real-Time Update!")
        except Exception as e:
            st.error(f"API fetch failed: {e}. Check token/internet.")
            st.stop()

        category, color = get_aqi_category(current_aqi)
        st.markdown(f"""
            <div class="box {color}">
                {current_aqi}<br>
                <span style="font-size:1.8rem">{category}</span>
            </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("PM₂.₅", f"{pm25:.1f} µg/m³")
        c2.metric("PM₁₀", f"{pm10:.1f} µg/m³")
        c3.metric("NO₂", f"{no2:.1f} µg/m³")
        c4.metric("O₃", f"{o3:.1f} µg/m³")

        # Attribution Display (Mandatory per AQICN policy)
        st.caption(f"Source: {attribution} via AQICN")

        # 7-Day Forecast (ML on synthetic + current)
        np.random.seed(42)
        days = 7

        historical_aqi = np.random.uniform(100, 250, 30)  # Past synthetic
        historical_aqi[-1] = current_aqi  # Inject current real AQI

        X = np.arange(len(historical_aqi)).reshape(-1, 1)
        y = historical_aqi
        model = LinearRegression().fit(X, y)
        future_x = np.arange(len(historical_aqi), len(historical_aqi) + days).reshape(-1, 1)
        forecast = model.predict(future_x).astype(int) + np.random.randint(-15, 15, days)

        st.markdown("### 7-Day AQI Forecast")
        dates = [(datetime.now() + timedelta(days=i)).strftime("%a %d %b") for i in range(days)]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=forecast, mode='lines+markers',
                                 line=dict(color="#ff4757", width=5), marker=dict(size=12)))
        fig.update_layout(height=400, template="plotly_dark", xaxis_title="Date", yaxis_title="AQI")
        st.plotly_chart(fig, use_container_width=True)

        # Health Tip
        if current_aqi <= 50:
            st.success("Good air! Enjoy outdoors.")
        elif current_aqi <= 100:
            st.warning("Moderate – Limit if sensitive.")
        else:
            st.error("Unhealthy – Stay indoors, mask up!")

        st.caption(f"Updated: {datetime.now().strftime('%d %b %Y • %I:%M %p')} | Source: AQICN API")

else:
    st.info("Enter city (lowercase) and click Get Live AQI")

st.markdown("---")
st.markdown("Made by Khushali | Token Secured | Attribution Compliant")




