from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List,Dict
import schema,crud,model
from Database import base,sessionlocal,engine


base.metadata.create_all(bind=engine)

app=FastAPI()

# dependency with the database
def get_obj():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return "Heloo User Welcome on Priyanshu Tiwari Project"
# 2- Get all Employee
@app.get('/employee',response_model=list[schema.EnployeeOut])
def get_employees(db:Session=Depends(get_obj)):
    return crud.getEmploye(db)



#3- Get Specific Employee
@app.get('/employee/{emp_id}',response_model=schema.EnployeeOut)
def getSEmploye(emp_id:int, db:Session=Depends(get_obj)):
    employee=crud.get_SEmploye(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

#1- Post Method
@app.post('/employee',response_model=schema.EnployeeOut)
def Create_Employee(employee:schema.EmployeCreate, db:Session=Depends(get_obj)):
   return crud.Create_Employe(db,employee)

# Udpdate
@app.put('/employee/{emp_id}', response_model=schema.EnployeeOut)
def updateEmp(emp_id:int, employee:schema.EmployeeUpdate, db:Session=Depends(get_obj)):
    db_employee=crud.update_Employee(db,emp_id,employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail='user not found')
    return db_employee




# Delte User 
@app.delete('/employee/{emp_id}', response_model=Dict[str,str])
def DeleteE(emp_id:int, db:Session=Depends(get_obj)):
    db_employee=crud.delete_employee(db,emp_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail='Error not Found')

    return {"detail": f'id= {emp_id} Data Delete succsefully'}


# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from Database import engine, sessionlocal,base
# from typing import List, Dict
# import  model,schema,crud


# base.metadata.create_all(bind=engine)

# app=FastAPI()

# # dependency with the database
# def get_db():
#     db=sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # endpoints

# #1- Post Method
# @app.post('/employee',response_model=schema.EnployeeOut)
# def Create_Employee(employee:schema.EmployeCreate, db:Session=Depends(get_db)):
#    return crud.Create_Employe(db,employee)


# # 2- Get all Employee
# @app.get('/employee',response_model=list[schema.EnployeeOut])
# def get_employees(db:Session=Depends(get_db)):
#     return crud.getEmploye(db)

# #3- Get Specific Employee
# @app.get('/employee/{emp_id}',response_model=schema.EnployeeOut)
# def getSEmploye(emp_id:int, db:Session=Depends(get_db)):
#     employee=crud.get_SEmploye(db,emp_id)
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# # 4 Update via Put
# @app.put('/employee/{emp_id}',response_model=schema.EnployeeOut)
# def Epm_update(emp_id:int, employee:schema.EmployeeUpdate, db:Session=Depends(get_db)):
#     db_employee=crud.update_Employee(db, emp_id, employee)

#     if db_employee is None:
#         raise  HTTPException(status_code=404, detail="Employee Not foumd")
#     return db_employee

# # 5 Delete
# @app.delete('/employee/{emp_id}', response_model=Dict[str, str])
# def delete_emp(emp_id:int, db:Session=Depends(get_db)):
#     employee=crud.delete_employee(db,emp_id)
#     if employee is None:
#             raise HTTPException(status_code=404, detail="Employee Not foumd")
#     return {'detail': 'Employee Deleted'}
    
    