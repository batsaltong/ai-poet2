#pip install python-dotenv
#pip install langchain-openai
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#환경 변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#Openai 모델 설정
chat_model = ChatOpenAI(api_key=api_key)

#streamlit UI 구성
st.title("AI시 생성기")
st.write("주제를 입력하면 AI가 맛있는 시를 호로록!")

#사용자 입력 받기
jujae = st.text_input("주제를 입력해주세요.")

prompt = f"{jujae}를 주제로 시를 써줄래, 윤동주 느낌으로"

#출력 드가자!!!!!
if jujae:
    try:
        response = chat_model.invoke(prompt)
        st.subheader("생선된 시")
        st.write(response.content)
    except Exception as e:
        st.error(f"오류 발생: {e}")

