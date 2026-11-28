from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableSequence

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")

model=ChatGroq(
    model="openai/gpt-oss-120b"
)

parser=StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel(
    {'joke': RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2, model, parser)}
)

final_chain=RunnableSequence(joke_chain,parallel_chain)

result=final_chain.invoke({'topic':'cricket'})

print(result)