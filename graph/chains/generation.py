import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

system_prompt = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise."""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Context: {context} \n\n Questions: {question}"),
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

generation_chain = prompt | llm | StrOutputParser()