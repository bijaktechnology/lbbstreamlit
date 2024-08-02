import streamlit as st
from streamlit_gsheets import GSheetsConnection


import pandas as pd
from ydata_profiling import ProfileReport

#report untul streamlit
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title ="Data Profiler Dashboard",
    page_icon ="⛈",
    layout = "wide",
    initial_sidebar_state="collapsed"
)

#----- Jdudul----

#st.title("Data Profiler")
st.markdown("<h1 style='text-align:center'>Data Profiler</hi>",unsafe_allow_html=True)
st.markdown("---")

#sidebar
with st.sidebar:
    st.subheader("Promotion Data")
    st.markdown("---")
    
if st.sidebar.button("Start Profiling Data"):
   #read Data
   conn = st.connection("gsheet", type=GSheetsConnection)
   
   df = conn.read(
       spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
       worksheet = st.secrets.gsheet_promotion["worksheet"]
   )
   #generate Report
   pr= ProfileReport(df)
   
   st_profile_report(pr)
