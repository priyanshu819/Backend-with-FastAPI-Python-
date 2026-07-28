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

# Export in Dectonery
temp1=patient.model_dump()
print(temp1)
print(type(temp1))

# Export in JSON
temp2=patient.model_dump_json()
print(temp2)
print(type(temp2))


# Coustomisation Export from dictonery
temp3=patient.model_dump(include=['name','age'])
print(temp3)
print(type(temp3))

# For exclude
# Coustomisation Export from dictonery
temp4=patient.model_dump(exclude=['name','age'])
print(temp4)
print(type(temp4))