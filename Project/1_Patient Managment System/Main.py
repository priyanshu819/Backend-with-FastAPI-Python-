from fastapi import FastAPI,HTTPException,Path, Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware # NAYA IMPORT

app=FastAPI()


#Allow for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credintial=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# Create a Pydantic Model
class Patient(BaseModel):
    id:Annotated[str,Field(..., description='This is unique identity of Patient', examples=['P001'])]
    name:Annotated[str,Field(..., description='This is name section of user')]
    age:Annotated[float, Field(..., gt=0, lt=100, description='this is age section Patient')]
    city:Annotated[str,Field(..., description='City of Patient')]
    gender:Annotated[Literal['male','female','other'], Field(..., description='Gender of the Ptient')]
    height:Annotated[float, Field(..., gt=0, description='height of patient')]
    weight:Annotated[float, Field(..., gt=0, description=' This is Patient weight')]



    # Compute BMI
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    # Compute Verdict 
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<20:
            return 'Normal'
        elif self.bmi<30:
            return 'Normal'
        else:
            return 'obese'



# Load The data from JSON File
def load_data():
    with open('Packege.json','r') as f:
        data=json.load(f)

    return data

# Add data in JSON FIle
def add_data(data):
    with open('Packege.json','w') as f:
        json.dump(data,f)



#--------------------------
#  Bukding  EndPoint
#--------------------------

# Create Home EndPoint
@app.get('/')
def home():
    return "Hello This is Home Page"


# Create EndPoint Use Post HTTP Method
@app.post('/create')
def create_function(patient:Patient):
 
    # step 1 -> load the data
    data=load_data()

    # step 2-> check data is exist or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient is alredy Exist')

    #export data from object to json
    data[patient.id]=patient.model_dump(exclude='id')

    # save the json file
    add_data(data)

    # After adding data successfuly give finally massage
    return  JSONResponse(status_code=201, content='message:Patient created successfully')



# Create the view add point
@app.get('/view')
def view():
    data=load_data()

    return data


# return data of specific patient
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(..., description='ID of the paitient in the DB', example='P001')):

    # load the data
    data = load_data()

    # check data visible or not
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='patient not found')



# Sorting by all patient
@app.get('/sort')
def sort_data(sort_by:str=Query(..., description='This is sorting feilds',examples=['height','weight','bmi']), order_by:str=Query(..., description='This order parameter',examples=['asc','desc'])):

    valied_fields=['height', 'weight', 'bmi']

    # now load the data
    data=load_data()

    # check valid feilds:
    if sort_by not in valied_fields:
        raise HTTPException(status_code=404, detail=f'please enter valid feilds from {valied_fields}')

    #check valid order
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=404, detail='please enter valid order from [asc, desc]')

    #now sort the data
    order= True if order_by=='desc' else False

    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=order)

    return sorted_data
    



