from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

adress_dict={'city':'Gurgaon','state':'Hariyana','pin':'12004'}

address1=Address(**adress_dict)

patient_dict={'name':'Priyanshu','gender':'Male','age':21,'address':address1}
patient=Patient(**patient_dict)

print(patient)

print(patient.address.city)
print(patient.address.state)
print(patient.address.pin)