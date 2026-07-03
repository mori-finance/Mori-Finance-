import streamlit as st
import pandas as pd

st.title("اختبار Mori Finance")

uploaded_file = st.file_uploader("ارفع الملف")

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("البيانات تم قراءتها بنجاح:")
        st.dataframe(df)
    except Exception as e:
        st.write("حصل خطأ:")
        st.write(e)


