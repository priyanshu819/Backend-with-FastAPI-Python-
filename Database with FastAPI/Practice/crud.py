
from sqlalchemy.orm import Session
import model, schema



def getEmploye(db:Session):
    return db.query(model.Employee).all()



def get_SEmploye(db:Session, emp_id:int):
    return db.query(model.Employee).filter(model.Employee.id==emp_id).first()


def Create_Employe(db:Session, employee:schema.EmployeCreate):
    db_employe=model.Employee(name=employee.name, email=employee.email)
    db.add(db_employe)
    db.commit()
    db.refresh(db_employe)
    return db_employe

def update_Employee(db:Session, emp_id:int, employee:schema.EmployeeUpdate):
    db_employee=db.query(model.Employee).filter(model.Employee.id==emp_id).first()
    if db_employee :
        if employee.name is not None:
            db_employee.name=employee.name
         
        if employee.email is not None:
            db_employee.email=employee.email
        db.commit()
        db.refresh(db_employee)

    return db_employee

def delete_employee(db:Session,emp_id:int):
    db_employee=db.query(model.Employee).filter(model.Employee.id==emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee