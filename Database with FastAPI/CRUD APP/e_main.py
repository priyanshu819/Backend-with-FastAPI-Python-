from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from a_database import engine, sessionlocal,base
from typing import List, Dict
import b_models,c_schemas,d_crud


base.metadata.create_all(bind=engine)

app=FastAPI()

# dependency with the database
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

# endpoints

#1- Post Method
@app.post('/employee',response_model=c_schemas.EnployeeOut)
def Create_Employee(employee:c_schemas.EmployeCreate, db:Session=Depends(get_db)):
   return d_crud.Create_Employe(db,employee)


# 2- Get all Employee
@app.get('/employee',response_model=list[c_schemas.EnployeeOut])
def get_employees(db:Session=Depends(get_db)):
    return d_crud.getEmploye(db)

#3- Get Specific Employee
@app.get('/employee/{emp_id}',response_model=c_schemas.EnployeeOut)
def getSEmploye(emp_id:int, db:Session=Depends(get_db)):
    employee=d_crud.get_SEmploye(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# 4 Update via Put
@app.put('/employee/{emp_id}',response_model=c_schemas.EnployeeOut)
def Epm_update(emp_id:int, employee:c_schemas.EmployeeUpdate, db:Session=Depends(get_db)):
    db_employee=d_crud.update_Employee(db, emp_id, employee)

    if db_employee is None:
        raise  HTTPException(status_code=404, detail="Employee Not foumd")
    return db_employee

# 5 Delete
@app.delete('/employee/{emp_id}', response_model=Dict[str, str])
def delete_emp(emp_id:int, db:Session=Depends(get_db)):
    employee=d_crud.delete_employee(db,emp_id)
    if employee is None:
            raise HTTPException(status_code=404, detail="Employee Not foumd")
    return {'detail': 'Employee Deleted'}
    
    