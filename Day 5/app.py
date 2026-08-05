import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Literal,Annotated
import pickle


# Import the ml model
with open('model.pkl','rb') as f:
    model=pickle.load(f)


app=FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


# Crearte a Pydantic Model To vailidate incoming data
class UserInput(BaseModel):
    age:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight:Annotated[float, Field(..., gt=0, description='weight of user')]
    height:Annotated[float, Field(..., gt=0, lt=2.5, description='Height of User')]
    income_lpa:Annotated[float, Field(..., gt=0, description='Annual Salary of User')]
    smoker:Annotated[bool, Field(..., description='Is user a smoker')]
    city:Annotated[str, Field(..., description='The City of the user')]
    occupation: Annotated[Literal['retired', 'freelancer','student','government_job','business_owner','unemployed','privat_job',], Field(..., description='What user do work')]


    # calculate BMI
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)

    # Lyfstyle risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi >30:
            return 'High'
        elif self.smoker and self.bmi  >27:
            return "Medium"
        else:
            return 'Low'


    # Compute Age Groupe
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"


    # City Tier Computed Fields
    @computed_field
    @property
    def city_tier(self)-> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3



# Create Predict Router(endpoint)
@app.post('/predict')
def predict_primium(data:UserInput):

    # Create Data Frame
    input_df=pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }])

    # Create Prediction code
    prediction=model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'Predicted Catogary is': prediction})
