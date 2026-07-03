import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mori Finance", layout="centered")

st.title("💼 Mori Finance")
st.write("المنصة الذكية للتحليل المالي")

# رفع الملف
uploaded_file = st.file_uploader("📂 ارفع ملف البيانات (Excel أو CSV)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # قراءة الملف
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.success("تم رفع الملف بنجاح!")
    
    # هنا بنحسب الأرقام من الملف نفسه (افترضنا وجود أعمدة باسم 'السيولة' و 'الربح')
    # لو ملفك فيه أسماء أعمدة مختلفة، قولي عشان أعدلهالك
    try:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="نسبة السيولة", value=f"{df['السيولة'].iloc[0]}")
        with col2:
            st.metric(label="نسبة الربحية", value=f"{df['الربح'].iloc[0]}%")
    except:
        st.warning("تأكد أن الملف يحتوي على أعمدة باسم 'السيولة' و 'الربح'")
else:
    st.info("💡 في انتظار رفع الملف لعرض النتائج الحقيقية.")


