import streamlit as st
import base64
import os

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Dashboard Access Hub",
    page_icon="📊",
    layout="wide"
)

# ==========================
# BACKGROUND FUNCTION
# ==========================
def set_background(image_path):
    if not os.path.exists(image_path):
        st.error(f"File background tidak ditemukan: {image_path}")
        return

    with open(image_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .dashboard-card {{
            background-color: rgba(255,255,255,0.85);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            transition: transform 0.2s;
            margin-bottom: 20px;
        }}

        .dashboard-card:hover {{
            transform: translateY(-5px);
        }}

        .dashboard-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #1f4e79;
        }}

        .dashboard-link {{
            text-decoration: none;
        }}

        button.dashboard-btn {{
            background-color: #1f4e79;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ==========================
# FOOTER LOGO FUNCTION
# ==========================
def footer_logo(image_path):
    if not os.path.exists(image_path):
        st.error(f"File logo tidak ditemukan: {image_path}")
        return

    with open(image_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <div style="margin-top:70px; margin-bottom:30px; text-align:center;">
            <img src="data:image/png;base64,{b64}" width="140"/>
            <p style="margin:10px 0 2px 0; font-size:14px; color:#333;">
                Developed by:
            </p>
            <p style="margin:0; font-size:15px; font-weight:bold; color:#1f4e79;">
                Business Intelligence Analyst Team
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================
# SET BACKGROUND
# ==========================
set_background("background.png")

# ==========================
# HEADER
# ==========================
st.markdown(
    "<h1 style='text-align:center; color:#1f4e79;'>Dashboard Access Hub</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#333;'>List Dashboard Monitoring</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# DASHBOARD LIST
# ==========================
dashboards = [
    {
        "title": "Weekly Report - SPV Performance",
        "link": "https://lookerstudio.google.com/reporting/261bcaba-fe01-4c49-9b3e-bc72bf7dbee1/page/JMfjF"
    },
    {
        "title": "Tactical for SPV (Salary Cost & Over Crew)",
        "link": "https://lookerstudio.google.com/reporting/1ebc1632-bce6-4aed-8568-e5b371230d67/page/p_7ygpse5oyd"
    },
    {
        "title": "Operational Cost All (COGS, Movement, COGM)",
        "link": "https://lookerstudio.google.com/reporting/1ef69901-4be4-43c8-a525-2939d660ec51/page/p_l6drp93lxd"
    }
]

# ==========================
# DISPLAY DASHBOARD CARDS
# ==========================
cols = st.columns(3)
for idx, dash in enumerate(dashboards):
    with cols[idx % 3]:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-title">{dash['title']}</div>
                <a class="dashboard-link" href="{dash['link']}" target="_blank">
                    <button class="dashboard-btn">Masuk ke Dashboard</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================
# FOOTER
# ==========================
footer_logo("logo-crk.png")
