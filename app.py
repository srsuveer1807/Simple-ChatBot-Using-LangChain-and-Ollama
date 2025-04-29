from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

from langsmith import traceable  # <-- Add this

# Load environment
load_dotenv()
os.environ["LANGCHAIN_PROJECT"] = "first-project"  # Just to be sure

# Langchain prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide responses to user queries."),
        ("user", "Question: {question}")
    ]
)

st.title("Langchain demo with Gemini")

input_text = st.text_input("Search the topic you want")

llm = Ollama(model="llama3")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

@traceable(name="chatbot_interaction")  # <-- LangSmith will log this run
def run_chain(question):
    return chain.invoke({"question": question})

if input_text:
    st.write(run_chain(input_text))
