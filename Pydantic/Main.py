from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# Type Validation

#  Step No -1
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=12, title='Name of the Patient',description='Give the name of the paiteint in less then 50 char', examples=['Nitish', 'Priyanshu'])]
    email:EmailStr
    linkdin_url:AnyUrl
    age:int=Field(ge=18)
    weight:Annotated[float,Field(get=0, strict=True)]
    married:bool =Annotated[bool,Field(default=None,description='Is the patient maaried or not')]  # this is default valuee
    allergies:Optional[list[str]] = None   # it is not required its is optional, None is default value
    contact:dict[str,str]

# Step No -2
Patient_info={'name':'Priyanshu Ti','email':'abcd@gamil.com','linkdin_url':"http://linkedin.com/1322",  'age':18, 'weight':72.5,  'contact':{'email':'abc@gamil.com', 'phone':'52634568'}}

patient1=Patient(**Patient_info)

# Step 3

def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.email)
    print(patient1.linkdin_url)
    print(patient1.age)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.allergies)
    print(patient1.contact)
    print('inserted')


insert_patient_data(patient1)