import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة عشان تبان "موبايل فيرست" وشيك
st.set_page_config(page_title="Mori Finance", layout="centered")

# 2. إضافة CSS عشان نلغي شكل "الابتدائي" ونعمل تصميم حديث (Dark/Modern)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { color: white; font-family: sans-serif; }
    div.stButton > button { width: 100%; border-radius: 10px; border: 1px solid #4CAF50; color: #4CAF50; }
    .big-font { font-size: 24px !important; font-weight: bold; color: #4CAF50; text-align: center; }
    .card { background-color: #262730; padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.5); }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر بشكل فخم
st.markdown('<p class="big-font">MORI FINANCE</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">التحليل المالي الذكي للشركات</p>', unsafe_allow_html=True)
st.write("---")

# 4. منطقة الرفع بشكل أنيق
st.markdown('<div class="card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📂 اسحب ملف الإكسيل هنا", type=['csv', 'xlsx'])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
    st.success("✅ تم تحليل البيانات بنجاح")
    st.dataframe(df.head(), use_container_width=True)
else:
    st.info("💡 المنصة جاهزة لاستقبال بياناتك.")
