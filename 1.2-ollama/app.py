import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM as Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions."),
        ("user", "Question:{question}")
    ]
)
st.title("Ollama with LangChain")
input_text = st.text_input("Enter your question:")
llm = Ollama(model="gemma:2b")
outputParser = StrOutputParser()
chain = prompt | llm | outputParser
if input_text:
    response = chain.invoke({"question": input_text})
    st.write("Answer:", response)