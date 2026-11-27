from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")

model=ChatGroq(
    model="openai/gpt-oss-120b"
)

class info(BaseModel):
    name : str =Field(discription="Name of the person")
    age : int =Field(discription='Age of the person')
    city : str =Field(discription='City of the person')

parser=PydanticOutputParser(pydantic_object=info)

template = PromptTemplate(
    template='give the name, age and city of a {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= template | model | parser

result = chain.invoke({'place':'Cristino Ronaldo'})

print(result)