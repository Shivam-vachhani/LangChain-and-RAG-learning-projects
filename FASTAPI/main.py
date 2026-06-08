from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        temp=json.load(f)
    return temp

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