from pydantic import BaseModel

class student(BaseModel):

    name: str
    branch:str

new_student={'name':'Arpit','branch':'ai'}

student=student(**new_student)

print(student)