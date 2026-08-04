from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
from fastapi.responses import JSONResponse
import json

app=FastAPI()

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
        if self.BMI_Calculate <18.5:
            return "underweight"
        elif self.BMI_Calculate <25:
            return "Normal"
        elif self.BMI_Calculate <30:
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



# --------------
# put method
#---------------

# Create a new pydantic model
class Patient_update(BaseModel):
        name:Annotated[Optional[str], Field(default=None)]
        city:Annotated[Optional[str], Field(default=None)]
        age:Annotated[Optional[int], Field(default=None)]
        gender:Annotated[Optional[Literal['male','female','other']], Field(default=None)]
        height:Annotated[Optional[float], Field(default=None,gt=0)]
        weight:Annotated[Optional[float], Field(default=None,gt=0)]


# create endPoint
@app.put('/edit/{patient_id}')
def update_patient(patient_id:str, patient_update:Patient_update):

    # load data
    data=load_data()

    # Check existing of patient id
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient Id not Found')

    # Extract patient data from file
    existing_data_info=data[patient_id]


    # Convert patient_update pydantic object into Dectionery
    # for munset only user send data come here otherwise all defult value come here
    updated_patient_info=patient_update.model_dump(exclude_unset=True)  
    for key,value in updated_patient_info.items():
        existing_data_info[key]=value


    # For BM and Verdict  we create a Patient Pydentic  Object and send this Existing value
    #  esistingdata -> Pydangtic object -> BMI + Verdict -> dictonery -> save 
    existing_data_info['id']=patient_id
    patient_pydantic_obj=Patient(**existing_data_info)

    #pydantic to dectionery
    existing_data_info=patient_pydantic_obj.model_dump(exclude={'id'})


    # now update this existing_patient_info in data
    data[patient_id]=existing_data_info 

    #save the data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'Patient updated successfully'})



#--------------------
#  DELETE Method
#--------------------

# Create a delete endPoint
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):

    # load data
    data=load_data()

    # check existing patiend_id
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient Not Found')

    # delete patient from data
    del data[patient_id]

    # save the data
    save_data(data)

    # Return Success message
    return JSONResponse(status_code=200, content={'message':'Patient deleted successfully'})

