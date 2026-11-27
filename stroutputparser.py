from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")

model=ChatGroq(
    model="openai/gpt-oss-120b"
)

template1=PromptTemplate(
    template="""
        Write a detailed report on the topic {topic}""",
        input_variables=['topic']
)

template2=PromptTemplate(
    template="""
        Write a 5 line summary on the following text. /n {text}""",
        input_variables=['text']
)

parser = StrOutputParser()

chain=template1 | model | parser |template2 | model |parser

result=chain.invoke({'topic': 'Black hole'})

print(result)
