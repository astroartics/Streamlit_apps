import streamlit as st
import pandas as pd
import numpy as np
import time

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')

placeholder = st.empty()
data=pd.DataFrame()

for i in range(101):
    progress_bar = st.progress(i)
    data = load_data(10000)
    time.sleep(0.05)
    progress_bar.empty()

data_load_state = st.text('Loading data...done!') 

#OPENAI_API_KEY = "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"
