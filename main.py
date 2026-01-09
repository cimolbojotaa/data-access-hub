import streamlit as st
import base64
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Data Access Hub",
    page_icon="📂",
    layout="wide"
)

# BACKGROUND FUNCTION
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
            background-color: rgba(255,255,255,0.88);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            transition: transform 0.2s;
            margin-bottom: 20px;
            min-height: 200px;
        }}

        

        .dashboard-card:hover {{
            transform: translateY(-10px);
        }}

        .dashboard-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #1f4e79;
        }}

        .dashboard-desc {{
            font-size: 14px;
            color: #444;
            margin-bottom: 15px;
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

# FOOTER LOGO FUNCTION
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

# SET BACKGROUND
set_background("background.png")

# HEADER
st.markdown(
    """
    <h1 style="
        text-align:center;
        color:#1f4e79; font-size: 35px;
        margin-bottom: 1px;
        margin-left: 30px
    ">
        Data Access Hub
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#333;
        margin-top: -15px;
    ">
        Akses Dashboard Monitoring & Form Operasional
    </p>
    """,
    unsafe_allow_html=True
)


st.markdown("<br>", unsafe_allow_html=True)

# DASHBOARD SECTION
st.markdown(
    "<h2 style='color:#1f4e79;font-size:28px;'>Dashboard Monitoring</h2>",
    unsafe_allow_html=True
)

dashboards = [
    {
        "title": "Weekly Report - SPV Performance",
        "desc": "Merekap performa mingguan SPV secara termasuk pencapaian operasional secara menyeluruh",
        "link": "https://lookerstudio.google.com/reporting/261bcaba-fe01-4c49-9b3e-bc72bf7dbee1/page/JMfjF"
    },
    {
        "title": "Tactical for SPV",
        "desc": "Monitoring COGM/S, movement stok, salary cost dan potensi over crew untuk pengambilan keputusan taktis di level SPV",
        "link": "https://lookerstudio.google.com/reporting/1ebc1632-bce6-4aed-8568-e5b371230d67/page/p_7ygpse5oyd"
    },
    {
        "title": "Operational Cost (COGS & COGM)",
        "desc": "Ringkasan biaya operasional meliputi COGM/S, profitabilitas, produktivitas manpower di level outlet",
        "link": "https://lookerstudio.google.com/reporting/1ef69901-4be4-43c8-a525-2939d660ec51/page/p_l6drp93lxd"
    },
    {
        "title": "Sales Report",
        "desc": "Rekap performa penjualan mencakup pencapaian sales, tren penjualan dan kontribusi outlet",
        "link": "https://lookerstudio.google.com/u/0/reporting/c5c55fd9-5274-4f02-a645-96742c76e894/page/h7PWF"
    }
]

cols = st.columns(4)
for idx, dash in enumerate(dashboards):
    with cols[idx % 4]:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-title">{dash['title']}</div>
                <div class="dashboard-desc">{dash['desc']}</div>
                <a href="{dash['link']}" target="_blank">
                    <button class="dashboard-btn">Masuk ke Dashboard</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# LARK FORM SECTION
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<h2 style='color:#1f4e79;font-size:28px;'>Lark Form Operasional</h2>",
    unsafe_allow_html=True
)

forms = [
    {
        "title": "Form Checkin Visit",
        "desc": "Form wajib untuk track kehadiran dan waktu awal visit ke outlet",
        "link": "https://bit.ly/checkin-visit"
    },
    {
        "title": "Form Checklist Visit",
        "desc": "Checklist kondisi outlet saat visit mencakup kepatuhan terhadap Standar Operasional",
        "link": "https://bit.ly/checklist-visit"
    },
    {
        "title": "Form Daily SO",
        "desc": "Form ini digunakan untuk mencatat jumlah stok fisik aktual di outlet pada hari berjalan",
        "link": "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjpUZoi1hjQ1yhBwl6uAifyAn"
    },
    {
        "title": "Absensi Crew",
        "desc": "Form absensi crew outlet (bersifat wajib) untuk mencatat kehadiran crew di outlet",
        "link": "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjpSN7FKBHSmH2inHXOwHaHEe"
    }
]

cols = st.columns(4)
for idx, form in enumerate(forms):
    with cols[idx % 4]:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-title">{form['title']}</div>
                <div class="dashboard-desc">{form['desc']}</div>
                <a href="{form['link']}" target="_blank">
                    <button class="dashboard-btn">Masuk ke Form</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# FOOTER
footer_logo("logo-crk.png")
