from pydantic import BaseModel,EmailStr
from typing import Optional

class student(BaseModel):

    name: str
    branch:str
    age : Optional[int]=18
    email :EmailStr

new_student={'name':'Arpit','branch':'ai','email':'abc@gmail.com'}

student=student(**new_student)

print(student.name)
print(student.branch)
print(student.age)
print(student.email)