import streamlit as st
import pandas as pd
import psutil
from streamlit_autorefresh import st_autorefresh

# Auto refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

st.set_page_config(
    page_title="AI Infrastructure Dashboard",
    layout="wide"
)

st.title("🚀 AI-Powered Infrastructure Monitoring & Auto-Healing Platform")

# Live Metrics
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{cpu}%")
    st.progress(int(cpu))

with col2:
    st.metric("Memory Usage", f"{memory}%")
    st.progress(int(memory))

with col3:
    st.metric("Disk Usage", f"{disk}%")
    st.progress(int(disk))

# Health Status
st.subheader("📊 System Health")

if disk > 90:
    st.error("🔴 Critical Disk Usage Detected")

elif disk > 70:
    st.warning("🟡 Disk Usage Increasing")

else:
    st.success("🟢 System Healthy")

# AI Analysis Section
st.subheader("🤖 Latest AI Analysis")

try:
    with open("logs/ai_analysis.log", "r", encoding="utf-8") as file:
        ai_analysis = file.read()

    st.info(ai_analysis)

except FileNotFoundError:
    st.warning("No AI Analysis Available Yet")

# Auto Healing Section
st.subheader("🛠 Auto-Healing Status")

try:
    with open("logs/healing.log", "r") as file:
        healing_status = file.read()

    st.success(healing_status)

except FileNotFoundError:
    st.warning("No Healing Activity Recorded Yet")
    
st.subheader("📋 Incident History")

try:
    incidents = pd.read_csv("logs/incidents.csv")

    st.dataframe(
        incidents.tail(10),
        use_container_width=True
    )

except FileNotFoundError:
    st.warning("No incidents recorded yet.")