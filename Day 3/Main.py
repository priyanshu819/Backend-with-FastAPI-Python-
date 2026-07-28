from fastapi import FastAPI, Path, HTTPException, Query
import json

app=FastAPI()

#  create a function read data from json file and use in when create endpoint
def load_data():
    with open('Packege.json','r') as f:
        data=json.load(f)
    return data


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
def view_paitent(patient_id:str=Path(..., description='ID of the paitient in the DB', example='P004')):

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
