import streamlit as st
from PIL import Image
import time
import numpy as np

# avatar_img = Image.open('sanjana_vector.png')
# st.chat_message("user",avatar = avatar_img).text("input")
st.chat_message("ai").text("Hey there, I'm WIAN - What's in a name 👋")

st.title("Chatbot")

message_back = """
<style>
.stAppHeader {display : none;}
.st-emotion-cache-h4xjwg {display : none;}
.e10jh26i0 {display : none;}
header {visibility : hidden;}
#chatbot {visibility : visible; width : 100%; font-size : 2.5rem; margin : 0; text-align : center; font-weight : 100; position : fixed; top : 0; left : 50%; transform : translate(-50%,0); z-index : 1; background-color : black;}
.st-emotion-cache-w9jsfw {color : black; font-size : 1.1em;}
.e1v02oy80 {color : white;}
.st-emotion-cache-janbn0 {background-color : rgb(105, 105, 105); box-shadow : inset 4px 4px 10px 0 rgba(0,0,0, 0.1), inset -4px -4px 10px 0 rgba(0,0,0, 0.1); border : 1.5px solid rgba(255,255,255,0.5)}
.st-emotion-cache-4oy321 {background-color : rgb(57, 59, 56); box-shadow : inset 2px 2px 8px 0 rgba(0,0,0, 0.1), inset -2px -2px 8px 0 rgba(0,0,0, 0.1); border : 1.5px solid rgba(255,255,255,0.5)}
</style>
"""
st.markdown(message_back,unsafe_allow_html = True)

if "messages" not in st.session_state :     # Initializing the messages history
    st.session_state.messages = []

if "responses" not in st.session_state :     # Initializing the response history
    st.session_state.responses = []    

avatar_img = Image.open('sanjana_vector.png')
for message,response in zip(st.session_state.messages,st.session_state.responses) : 
    st.chat_message(message['role'], avatar=avatar_img).text(message['content'])
    st.chat_message(response['role']).text(response['content'])

response = np.random.randn(1)

if prompt := st.chat_input("What is up?") :
    st.chat_message("user",avatar = avatar_img).text(prompt)
    st.session_state.messages.append({'role' : 'user', 'content' : prompt})
    st.chat_message("ai").text(response)   
    st.session_state.responses.append({'role' : 'ai', 'content' : response})