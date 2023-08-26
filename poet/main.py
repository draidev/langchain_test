#from dotenv import load_dotenv
#load_dotenv()

# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI

# model = ChatOpenAI(openai_api_key="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")
# content="인간"

# result = model.predict(content)
# #llm = OpenAI(openai_api_key="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")

# #result = llm.predict("hi")
# print(result)


import streamlit as st

st.title('나는야 챗 시인이다')

content = st.text_input('시의 주제를 알려주세요 title')
st.write('시의 주제는?', content)