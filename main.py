import streamlit as st
import pandas as pd

# --- إعدادات الصفحة والمظهر للموقع ---
st.set_page_config(
    page_title="Mori Finance | التحليل المالي الذكي",
    page_icon="📊",
    layout="wide"
)

# --- تخصيص الألوان والهوية البصرية ---
st.markdown("""
<style>
    .main-title { font-size:38px !important; color:#2E86C1; }
    .subtitle { font-size:18px !important; color:#566573; }
    .report-box { background-color: #EFF6FF; padding: 20px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💼 Mori Finance</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">المنصة الذكية للتحليل المالي للشركات</div>', unsafe_allow_html=True)
st.write("---")

# --- لوحة التحكم الجانبية ---
with st.sidebar:
    st.header("Mori Control Panel")
    st.info("مرحباً بك في النسخة التجريبية (MVP)")
    uploaded_file = st.file_uploader("ارفع ملف البيانات المالية", type=['csv', 'xlsx'])
    st.write("---")
    st.caption("2026 © بيانات مشفرة وآمنة تماماً")

# --- محاكاة البيانات لتظهر للعميل فور دخوله ---
company_name = "مؤسسة العميل الموقرة"
liquidity_data = {"نسبة النقدية": 1.4, "نسبة التداول": 2.5}
profitability_data = {"العائد على الأصول": 15.0, "هامش الربح": 22.5}

st.subheader(f"تقرير تحليل الأداء لـ {company_name}")
col1, col2 = st.columns(2)

with col1:
    st.write("### مؤشرات السيولة")
    st.bar_chart(liquidity_data)

with col2:
    st.write("### مؤشرات الربحية")
    st.bar_chart(profitability_data)
