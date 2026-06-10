from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse 
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Provide unique use id to patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="Provide Name of user")]
    age:Annotated[int,Field(...,gt=0,description="Age of the patient")]
    gender:Annotated[Literal["male",'female','others'],Field(...,description="Gender of patient")]
    height:Annotated[float,Field(...,gt=0,description="Hight of patient in meters")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of patient in kgs")]

    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.0:
            return "Underweight"
        elif self.bmi < 25 :
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        temp=json.load(f)
    return temp

def add_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message":"Patients managment system API"}

@app.get("/about")
def about():
    return {"message":"This Project is about Patients managment"}

@app.get("/view")
def view_patients():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(...,description="Provide patient's id to get info",example="P001") ):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")

@app.get("/sort")
def sort_data(sort_by:str = Query(...,description="Sort baaised on height weight or bmi"),
              order:str = Query('asc',description="sort data either ascending or decending")):
    
    valid_feild =['height','weight','bmi']
    if sort_by not in valid_feild:
        raise HTTPException(status_code=400,detail="invalid feild selected  from {valid_feild}")
    
    valid_order = ['asc','desc']
    if order not in valid_order:
            raise HTTPException(status_code=400,detail="invalid feild selected  from {valid_order}")
    
    data = load_data()

    sort_order=True if order == 'desc' else False

    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.post('/add_patient')
def create_patient(req:Patient):
    data = load_data()

    if req.id in data:
        raise HTTPException(status_code=400,detail="Patient already exists")
    
    data[req.id] = req.model_dump(exclude=["id"])

    add_data(data)

    return JSONResponse(status_code=201,content={"message":"Patient created successfully","data":data})

