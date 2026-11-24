from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class student(BaseModel):

    name: str
    branch:str
    # it is for the optional purpose put age or else it will default to 18
    age : Optional[int]=18
    #used for correct email check
    email :EmailStr
    #Used for the condition
    cgpa : float=Field(gt=0,lt=10,default=5.0,description='A number which represents the cgpa of the person') 

new_student={'name':'Arpit','branch':'ai','email':'abc@gmail.com','cgpa':8.5}

student=student(**new_student)

print(student.name)
print(student.branch)
print(student.age)
print(student.email)
print(student.cgpa)

# Now by this we can access the items like the simple dictionary
student_dict=dict(new_student)
print(student_dict['cgpa'])