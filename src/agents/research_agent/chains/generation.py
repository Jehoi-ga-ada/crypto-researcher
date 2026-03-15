from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langsmith import Client

client = Client()
llm = ChatOllama(model="deepseek-r1:8b", temperature=0)
prompt = client.pull_prompt("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()