from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated


'''
   We have to check email of the user that user belongs to hdfc, icici banck or not ?

   so we have to use Feild Validators to create custoume data validation

'''

#  Step No -1
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validation(cls, value):
        valid_domains=['hdfc.com','icici.com']

        #abc@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domain')

        return value

    # tranform name as Capita letter of User
    @field_validator('name')
    @classmethod
    def covert_capital(cls,value):
        return value.upper()


    # Check the age validation  eg-> before
    # Check age between 0 to 100
    @field_validator('age', mode='after')
    #@field_validator('age', mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0< value < 100:
            return value
        else:
            return ValueError('Age Should be in Betqween 0 and 100')


        

# Step No -2
Patient_info={'name':'Priyanshu Tiwari','email':'priyanshu@icici.com','age':'20','weight':75.5,'married':True,'allergies':['pillon','Dust'], 'contact':{'phone':'8485','email':'pri@gmail.com'}}

patient1=Patient(**Patient_info)

#Step-3

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