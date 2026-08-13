from pydantic import BaseModel, EmailStr

class EmployeBase(BaseModel):
    name:str
    email:EmailStr


class EmployeCreate(EmployeBase):
    pass
class EmployeeUpdate(EmployeBase):
    pass

class EnployeeOut(EmployeBase):
    id:int

    class Config:
        orm_mode=True