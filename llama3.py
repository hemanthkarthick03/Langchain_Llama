import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load environment variables
load_dotenv()

# Set environment variables for Langchain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "App-LLM"
os.environ["LANGCHAIN_API_KEY"] = "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"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please ask me any questions !!!"),
        ("user", "Question: {question}")
    ]
)

# Initialize Streamlit
st.title("Langchain Demo with Llama")
input_text = st.text_input("Question need to be searched: ")

# Ollama LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Main functionality
if input_text:
    try:
        result = chain.invoke({"question": input_text})
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {e}")
