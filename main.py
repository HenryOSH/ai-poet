# -*- coding: utf-8 -*-
import streamlit as st

#from dotenv import load_dotenv
#load_dotenv()
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')



if st.button('시 작성 요청하기'):
    with st.spinner('인공지능이 시를 작성중입니다! 조금만 기다려주세요..'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)




