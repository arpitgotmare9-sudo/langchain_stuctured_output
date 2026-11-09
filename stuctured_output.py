from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from pathlib import Path

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")


model=ChatGroq(
    model="openai/gpt-oss-120b"
)

# schema
class review(TypedDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return the sentiment of the review either negative ,positive or neutral"]

structured_model=model.with_structured_output(review)

result=structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

#print(result)
print(result['sentiment'])
print(result['summary'])