
from pydantic import BaseModel, EmailStr,ConfigDict
from typing import Optional

class EmployeBase(BaseModel):
    name:str
    email:EmailStr


class EmployeCreate(EmployeBase):
    pass
class EmployeeUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[EmailStr]=None 

class EnployeeOut(EmployeBase):
    id:int

    class Config:
       model_config=ConfigDict(from_attributes=True)