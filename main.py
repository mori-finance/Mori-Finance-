import streamlit as st

st.set_page_config(page_title="Mori Finance", layout="centered")

# تحسين التنسيق بشكل مباشر وبسيط لضمان وضوح النصوص
st.markdown("""
    <style>
    .main-title { color: #002244; text-align: center; font-size: 3rem; }
    .sub-title { color: #555; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Mori Finance</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">المنصة الذكية للتحليل المالي</p>', unsafe_allow_html=True)

st.write("---")

# استخدام واجهة Streamlit القياسية (أنظف وأضمن على الموبايل)
col1, col2 = st.columns(2)
with col1:
    st.metric(label="نسبة التداول", value="2.5", delta="0.2")
with col2:
    st.metric(label="هامش الربح", value="22.5%", delta="1.5%")

st.info("قم برفع ملف البيانات المالية للبدء في التحليل.")

