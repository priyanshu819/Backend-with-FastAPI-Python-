from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware # NAYA IMPORT

app = FastAPI()

# NAYA CODE: CORS ko allow karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Har jagah se request allow karega
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create a Pydantic Model
class Patient(BaseModel):
    id:Annotated[str,Field(..., description='Id of the patients', examples=["P001"])]
    name:Annotated[str, Field(..., description="Name of the Patient")]
    city:Annotated[str, Field(...,description="City of the Patient")]
    age:Annotated[int, Field(..., gt=0,lt=100,description="Age of the Patient")]
    gender:Annotated[Literal['male','female','other'],Field(..., description='Gender Of the Patient')]
    height:Annotated[float,Field(..., gt=0, description='Height Of the Patient in mtr')]
    weight:Annotated[float, Field(..., gt=0, description='Weight of the Patient in Kgs')]


    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi <18.5:
            return "underweight"
        elif self.bmi<25:
            return "Normal"
        elif self.bmi<30:
            return "Normal"
        else:
            return "Obese"



#  create a function read data from json file and use in when create endpoint
def load_data():
    with open('Packege.json','r') as f:
        data=json.load(f)
    return data

# Add data in JSON File
def save_data(data):
        with open('Packege.json','w') as f:
            json.dump(data, f)
    


@app.get("/")
def hello():
    return{'message':'Paitient Managment System API'}

@app.get('/about')
def about():
    return{'message':'A fully functional API manage your patiet records'}

# Create view endpoint..
@app.get('/view')
def view():
    data=load_data()

    return data

#  Day Four Lecturessss....

@app.get('/patient/{patient_id}')
def view_paitent(patient_id:str=Path(..., description='ID of the paitient in the DB', examples='P004')):

    #load all the data
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")



#  Create endpoint for sorting query
@app.get('/sort')
def sort_patient(sort_by:str = Query(..., description='sort on besis of height , weight and BMI '), order:str=Query('asc', description='sort in assending or decsending order')):
    valid_feilds=['height','weight','bmi']

    if sort_by not in valid_feilds:
        raise HTTPException(status_code=404, detail=f'Invalid feild select from {valid_feilds}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=404, detail=f'Invalid feild select from [asc, desc]')

    data=load_data()
    sort_order= True if order=='desc' else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)

    return sorted_data



@app.post('/create')
def create_function(patient:Patient):

    # load existing data
    data=load_data()


    # check if patient alerady exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient Alredy Exist')

    #-----------------
    # add new patient 
    #----------------

    # export pydantic object into dectonery
    data[patient.id]=patient.model_dump(exclude='id')

    # save into json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient created successfully'})

