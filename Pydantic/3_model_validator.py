from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict

#  Step No -1
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]


    # Create a Model validator
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError('Patients older than 60 must have an Emergency number:')
        return model

# Step No -2
Patient_info={'name':'Priyanshu Tiwari','email':'priyanshu@icici.com','age':'50','weight':75.5,'married':True,'allergies':['pillon','Dust'], 'contact':{'phone':'8485','email':'pri@gmail.com'}}

patient1=Patient(**Patient_info)


# Step no 3
def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.email)
     
    print(patient1.age)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.allergies)
    print(patient1.contact)
    print('inserted')


insert_patient_data(patient1)