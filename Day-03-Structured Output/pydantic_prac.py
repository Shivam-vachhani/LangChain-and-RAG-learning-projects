from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Person X'
    age: Optional[int] = None
    email:EmailStr
    cgpe:float = Field(gt=0,lt=10,default=5,description='tha cgpe comes from the collage marksheet ')

student_dict = {'name':'Sekiro','age':32,'email':'hello@gmail.com','cgpe':9}

student1 = Student(**student_dict)

student_dict = dict(student1)

print(student_dict)

student_json = student1.model_dump_json()

student_json.save()
