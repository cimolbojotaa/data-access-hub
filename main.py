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
        """
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .dashboard-card {
            background-color: rgba(255,255,255,0.88);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            transition: transform 0.2s;
            margin-bottom: 20px;
            min-height: 200px;
        }

        .dashboard-card:hover {
            transform: translateY(-10px);
        }

        .dashboard-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #1f4e79;
        }

        .dashboard-desc {
            font-size: 14px;
            color: #444;
            margin-bottom: 15px;
        }

        button.dashboard-btn {
            background-color: #1f4e79;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        </style>
        """ % b64,
        unsafe_allow_html=True
    )

# FOOTER FUNCTION
def footer_logo(image_path):
    if not os.path.exists(image_path):
        st.error(f"File logo tidak ditemukan: {image_path}")
        return

    with open(image_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    st.markdown(
        """
        <div style="margin-top:70px; margin-bottom:30px; text-align:center;">
            <img src="data:image/png;base64,%s" width="140"/>
            <p style="margin:10px 0 2px 0; font-size:14px; color:#333;">
                Developed by:
            </p>
            <p style="margin:0; font-size:15px; font-weight:bold; color:#1f4e79;">
                Business Intelligence Analyst Team
            </p>
        </div>
        """ % b64,
        unsafe_allow_html=True
    )

# INIT
set_background("background.png")

# HEADER
st.markdown(
    """
    <h1 style="text-align:center;color:#1f4e79;font-size:35px;margin-bottom:1px;">
        Data Access Hub
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="text-align:center;color:#333;margin-top:-15px;">
        Akses Dashboard Monitoring & Form Operasional
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# DASHBOARD MONITORING
st.markdown(
    "<h2 style='color:#1f4e79;font-size:28px;'>Dashboard Monitoring</h2>",
    unsafe_allow_html=True
)

dashboards = [
    ("Weekly Report - SPV Performance",
     "Merekap performa mingguan SPV termasuk pencapaian operasional secara menyeluruh",
     "https://lookerstudio.google.com/reporting/261bcaba-fe01-4c49-9b3e-bc72bf7dbee1/page/JMfjF"),

    ("Tactical for SPV",
     "Monitoring COGM/S, movement stok, salary cost dan potensi over crew untuk keputusan taktis SPV",
     "https://lookerstudio.google.com/reporting/1ebc1632-bce6-4aed-8568-e5b371230d67/page/p_7ygpse5oyd"),

    ("Operational Cost (COGS & COGM)",
     "Ringkasan biaya operasional, profitabilitas dan produktivitas manpower outlet",
     "https://lookerstudio.google.com/reporting/1ef69901-4be4-43c8-a525-2939d660ec51/page/p_l6drp93lxd"),

    ("Sales Report",
     "Rekap performa penjualan, tren sales dan kontribusi outlet termasuk frozen",
     "https://lookerstudio.google.com/u/0/reporting/c5c55fd9-5274-4f02-a645-96742c76e894/page/h7PWF")
]

cols = st.columns(4)
for i, d in enumerate(dashboards):
    with cols[i % 4]:
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="dashboard-title">%s</div>
                <div class="dashboard-desc">%s</div>
                <a href="%s" target="_blank">
                    <button class="dashboard-btn">Masuk ke Dashboard</button>
                </a>
            </div>
            """ % d,
            unsafe_allow_html=True
        )

# LARK FORM OPERASIONAL
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<h2 style='color:#1f4e79;font-size:28px;'>Lark Form Operasional</h2>",
    unsafe_allow_html=True
)

forms = [
    ("Form Checkin Visit",
     "Form wajib untuk track kehadiran dan waktu awal visit outlet",
     "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjp02svHWWRHHRLTxS8RMyllh"),

    ("Form Checklist Visit",
     "Checklist kondisi outlet saat visit sesuai Standar Operasional",
     "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjpbU0BNIgf90d0huOyM0pm7f"),

    ("Form Daily SO",
     "Pencatatan stok fisik aktual outlet harian",
     "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjpUZoi1hjQ1yhBwl6uAifyAn"),

    ("Absensi Crew",
     "Form absensi crew outlet (wajib)",
     "https://ajp0nod3vmbt.jp.larksuite.com/share/base/form/shrjpSN7FKBHSmH2inHXOwHaHEe")
]

cols = st.columns(4)
for i, f in enumerate(forms):
    with cols[i % 4]:
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="dashboard-title">%s</div>
                <div class="dashboard-desc">%s</div>
                <a href="%s" target="_blank">
                    <button class="dashboard-btn">Masuk ke Form</button>
                </a>
            </div>
            """ % f,
            unsafe_allow_html=True
        )

# BASE DETAIL DATA LARK
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<h2 style='color:#1f4e79;font-size:28px;'>Base Detail Data Lark</h2>",
    unsafe_allow_html=True
)

bases = [
    ("Base Sales Performance",
     "Base weekly report yang digunakan di weekly meeting with direksi Operasional (wajib dipertanggungjawabkan SPV)",
     "https://ajp0nod3vmbt.jp.larksuite.com/wiki/Jb1Zw8smWibCqpk1AdwjbMWPpxS?table=tbl1CLCTZn1lmUPr&view=vew1uDZAcG"),

    ("Base Operation Data",
     "Base data absensi crew outlet",
     "https://ajp0nod3vmbt.jp.larksuite.com/base/F8fcbvH5laRyjXsyCIzjSsMtpEc?table=tblORWtxOY7Tr5gk&view=vewUjIK5gJ")
]

cols = st.columns(4)
for i, b in enumerate(bases):
    with cols[i % 4]:
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="dashboard-title">%s</div>
                <div class="dashboard-desc">%s</div>
                <a href="%s" target="_blank">
                    <button class="dashboard-btn">Masuk ke Base</button>
                </a>
            </div>
            """ % b,
            unsafe_allow_html=True
        )

# FOOTER
footer_logo("logo-crk.png")