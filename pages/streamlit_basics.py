import streamlit as st

st.write('Hello World!')
st.title("Hello World")

# -----------------------

import pandas as pd

dataframe = pd.DataFrame({
    'first' : [1,2,3,4],
    'second' : [5,6,7,8]
})
dataframe

# st.write("OK")
# Unlike st.write() other methods return an object that can be used and modified, either by adding data to it or replacing it [st.write() can display data of any type].

# -----------------------

import numpy as np

df = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' %i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))

# st.table(df)

# -----------------------

line_chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
    )
st.line_chart(line_chart_data)


map_data = pd.DataFrame(
    np.random.randn(200, 2) + [20.5937, 78.9629],
    columns=['lat', 'lon'])
st.map(map_data)

# -----------------------

# Widgets
x = st.slider('Number')
st.write(x, 'squared is', x*x)

st.text_input("Enter your name and press enter", key="your_name")
st.session_state.your_name

if st.checkbox('Show DataFrame'):
    df

option = st.selectbox(
    'Which number do you like best?',
     dataframe['first'])
option

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# -----------------------

import streamlit as st

left_column, right_column = st.columns(2)
left_column.button('Press me!')

# Calling Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


# import time
# 'Computation started...'
# bar = st.progress(0)
# for i in range(100):
#   bar.progress(i + 1)
#   time.sleep(0.1)
# 'And we\'re done!'

# -----------------------