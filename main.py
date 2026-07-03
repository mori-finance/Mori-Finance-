import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Mori Finance | التحليل الذكي", page_icon="📊", layout="wide")

# تصميم احترافي بـ CSS
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .css-1r6slp0 { padding: 2rem; }
    .card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px; 
    }
    .title { color: #1e3a8a; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<h1 class="title">💼 Mori Finance</h1>', unsafe_allow_html=True)
st.markdown('#### 🚀 المنصة الذكية للتحليل المالي للشركات')
st.write("---")

# لوحة التحكم الجانبية
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    uploaded_file = st.file_uploader("📂 ارفع ملف البيانات المالية", type=['csv', 'xlsx'])
    st.write("---")
    st.success("المنصة جاهزة للتحليل")

# عرض البيانات في كروت
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>💧 مؤشرات السيولة</h3></div>', unsafe_allow_html=True)
    st.bar_chart({"نسبة التداول": 2.5, "نسبة النقدية": 1.4})

with col2:
    st.markdown('<div class="card"><h3>📈 مؤشرات الربحية</h3></div>', unsafe_allow_html=True)
    st.bar_chart({"العائد على الأصول": 15.0, "هامش الربح": 22.5})

st.info("💡 نصيحة: ارفع ملف البيانات للحصول على تحليل مخصص لشركتك.")

