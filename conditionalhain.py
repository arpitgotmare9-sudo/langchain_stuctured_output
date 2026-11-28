from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")

model=ChatGroq(
    model="openai/gpt-oss-120b"
)

parser=StrOutputParser()

class feedback(BaseModel):

    sentiment : Literal['Positive','Negative']=Field(description='Give the sentiment of the feedback')

parser1=PydanticOutputParser(pydantic_object=feedback)


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)

classifier_chian= prompt1 | model | parser1

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt3 | model |parser),
    RunnableLambda(lambda x:'Could not recognize the sentiment')
)

final_chain= classifier_chian | branch_chain

result=final_chain.invoke({'feedback':'THis is a terrible product'})

print(result)