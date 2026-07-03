import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mori Finance", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Mori Finance</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("ارفع ملف الإكسيل هنا", type=['xlsx', 'csv'])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
        st.write("### البيانات:")
        st.dataframe(df)
    except Exception as e:
        st.error("فيه مشكلة في قراءة الملف، تأكد إنه ملف إكسيل سليم.")
else:
    st.write("بانتظار رفع الملف...")

