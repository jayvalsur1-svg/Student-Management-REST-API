from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,computed_field,field_validator,Field
from typing import Annotated,Dict,Optional
class Student(BaseModel):
    id:Annotated[str,Field(description="Id value in here",examples=['S001'])]
    name:Annotated[str,Field(description="Name in here",examples=['Luffy'])]
    grade_level:Annotated[int,Field(gt=0,lt=13,description="Enter your current grade",examples=[6])]
    subjects:Annotated[Dict[str,int],Field(description="Subject name and marks in that dictonary",examples=[{'Maths':32,}])]

    @field_validator('id')
    @classmethod
    def id_value(cls,value):
        if isinstance(value,str):
            if not value.startswith('S00'):
                raise ValueError('ID must start with S00')
        return value

    @field_validator('subjects')
    @classmethod
    def subject(cls,value):
        if isinstance(value,dict):
            for subject,score in value.items():
                if not (0<=score<=100):
                    raise ValueError('Your data are miss mach in api terms')
        return value

    @computed_field
    @property
    def persantage(self)->float:
        if not self.subjects:
            return 0.0
        student_total_marks=sum(self.subjects.values())
        number_of_sub=len(self.subjects)
        total_subject_marks=number_of_sub*100
        per=(student_total_marks/total_subject_marks)*100
        return per
    @computed_field
    @property
    def status(self)->str:
        if self.persantage<=43:
            return "Pass"
        elif self.persantage<=55:
            return "D"
        elif self.persantage<=65:
            return'C'
        elif self.persantage<=75:
            return "B"
        elif self.persantage<=85:
            return "A"
        elif self.persantage<=99:
            return "S"
        else:
            return "Fail"

    @computed_field
    @property
    def CGPA(self)->float:
        cgpa=self.persantage/10
        return cgpa

    @computed_field
    @property
    def Top_subjects(self)-> str:
        if not self.subjects:
            return "N/A"
        return max(self.subjects,key=self.subjects.get)

class student_update(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    grade_level:Annotated[Optional[int],Field(default=None)]
    subjects:Annotated[Optional[Dict[str,int]],Field(default=None)]

App=FastAPI()
@App.get('/')
def defaut():
    return {'Message':"homepage"}
def load_data():
    with open('data.json','r') as Y:
        data=json.load(Y)
    return data
def save(data):
    with open('data.json','w') as A:
        json.dump(data,A)
@App.get('/view')
def view():
    data=load_data()
    return data
@App.get('/student/{id}')
def student_data(id:str):
    data=load_data()
    if id not in data:
        return JSONResponse(status_code=404,content="This id not found in Data base")
    return data[id]
@App.post('/add')
def add_student(student:Student):
    data=load_data()
    if student.id in data:
        return JSONResponse(status_code=400,content="This id already exists in the Data base")
    data[student.id]=student.model_dump(exclude={'id'})
    save(data)
    return JSONResponse(status_code=200,content="Your student added in database")
@App.put('/update/{id}')
def update_student(id:str,student:student_update):
    data=load_data()
    if id not in data:
        return JSONResponse(status_code=404,content="This id not found in Data base")
    studentInfo=data[id]
    update_student_info=student.model_dump(exclude_unset=True)
    for key,value in update_student_info.items():
        studentInfo[key]=value
    studentInfo['id']=id
    student_obj=Student(**studentInfo)
    studentInfo=student_obj.model_dump(exclude={'id'})
    data[id]=studentInfo
    save(data)
    return JSONResponse(status_code=200,content={'message':'updated sucessfuly'})


@App.delete('/delete/{id}')
def delete_student(id:str):
    data=load_data()
    if id not in data:
        return JSONResponse(status_code=404,content="This id not found in Data base")
    del data[id]
    save(data)
    return JSONResponse(status_code=200,content="Your student deleted in database")