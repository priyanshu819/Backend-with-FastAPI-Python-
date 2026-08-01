from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Literal
import json



# Create a Pydantic Model
class Patient(BaseModel):
    id:Annotated[str,Field(..., description='This is unique identity of Patient', examples=['P001'])]
    name:Annotated[str,Field(..., description='This is name section of user')]
    age:Annotated[float, Field(..., gt=0, lt=100, description='this is age section Patient')]
    cit:Annotated[str,Field(..., description='City of Patient')]
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





