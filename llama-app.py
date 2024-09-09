from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
<<<<<<< HEAD:Chatbot/llama-app.py
os.environ["LANGCHAIN_PROJECT"]="App-LLM"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
=======
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
>>>>>>> d934943eec087cb615a61adc096ec4d0c9d7bda9:llama-app.py

## Prompt Template

prompt=ChatPromptTemplate.from_messages (
    [
        ("system", "You are a helpful assistant. Please ask me any questions !!!"),
        ("user", "Question: {question}")
    ]
)

# Streamlit
st.title("Langchain Demo with Llama")
input_text = st.text_input("Question need to be searched: ")

# Ollama LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
<<<<<<< HEAD:Chatbot/llama-app.py
    st.markdown(chain.invoke({"question": input_text}))
=======
    st.write(chain.invoke({"question": input_text}))
>>>>>>> d934943eec087cb615a61adc096ec4d0c9d7bda9:llama-app.py
