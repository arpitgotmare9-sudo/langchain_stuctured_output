from pydantic import BaseModel
from typing import Optional

class student(BaseModel):

    name: str
    branch:str
    age : Optional[int]=18

new_student={'name':'Arpit','branch':'ai'}

student=student(**new_student)

print(student.name)
print(student.branch)
print(student.age)