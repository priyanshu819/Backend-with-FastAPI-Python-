from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

#  Step No -1
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float  #kgs
    height:float  #mtr
    married:bool
    allergies:List[str]
    contact:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)-> float:
        bmi=(self.weight/(self.height**2),2)
        return bmi






# Step No -2
Patient_info={'name':'Priyanshu Tiwari','email':'priyanshu@icici.com','age':'50','weight':75.5,'height':4.5,'married':True,'allergies':['pillon','Dust'], 'contact':{'phone':'8485','email':'pri@gmail.com'}}

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

def update_data(paiteint1):
    print("BMI:",paiteint1.calculate_bmi)
    print('updated....')


insert_patient_data(patient1)
update_data(patient1)