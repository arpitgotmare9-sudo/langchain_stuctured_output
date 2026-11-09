from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
from pathlib import Path

load_dotenv()

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")


model=ChatGroq(
    model="openai/gpt-oss-120b"
)

# schema
class review(TypedDict):
    key:Annotated[list[str],"Write down all the key attributes mentioned in the review in the list"]
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return the sentiment of the review either negative ,positive or neutral"]
    pros:Annotated[Optional[list[str]],"Write all the pros mentioned in the review in the form of list"]
    corns:Annotated[Optional[list[str]],"Write down all the corns present in the review in the form of list"]

structured_model=model.with_structured_output(review)

result=structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")
#print(result)
print(result['sentiment'])
print(result['summary'])
print(result['pros'])
print(result['corns'])
print(result['key'])