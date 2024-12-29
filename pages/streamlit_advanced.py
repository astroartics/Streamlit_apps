import streamlit as st
import pandas as pd
import numpy as np

# This decoration stores the result returned by this function, and displays result from cache, unless the function code or parameters are changed.
@st.cache_data
def cache_func_example(param1):
    return param1

function_returned = cache_func_example(2)
function_returned


# Widgets handle their statefulness all by themselves
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

if "df2" not in st.session_state:
    st.session_state.df2 = pd.DataFrame(np.random.randn(20,2),columns=["x","y"])

st.header("Choose a colour")
color = st.color_picker("Color","#FF0000")
st.divider()    
st.scatter_chart(st.session_state.df2,x="x",y="y",color=color)

# -----------------------

# Database connectivity
from sqlalchemy.sql import text
conn = st.connection('postgres',type="sql")
db_table_data = conn.query("Select *from test;")
db_table_data

# with conn.session as s:
#     s.execute(text("insert into test values(6);"))
#     s.commit()
data = conn.session.execute(text("Select *from test;")).fetchall()    
st.table(data)