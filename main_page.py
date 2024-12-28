import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stToolbarActions {visibility: hidden;}
.st-emotion-cache-1p1m4ay {visibility: hidden;}
.e3i9eg82 {visibility: hidden;}
._container_gzau3_1 _viewerBadge_nim44_23 {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 