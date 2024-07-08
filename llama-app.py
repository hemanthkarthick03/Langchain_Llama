from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]="App-LLM"
os.environ["LANGCHAIN_API_KEY"] = "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"

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
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))