from sqlalchemy.orm import Session
import b_models, c_schemas



def getEmploye(db:Session):
    return db.query(b_models.Employee).all()



def get_SEmploye(db:Session, emp_id:int):
    db.query(b_models.Employee).filter(b_models.Employee.id==emp_id).first()


def Create_Employe(db:Session, employee:c_schemas.EmployeCreate):
    db_employe=b_models.Employee(name=employee.name, email=employee.email)
    db.add(db_employe)
    db.commit()
    db.refresh(db_employe)
    return db_employe

def update_Employee(db:Session, emp_id:int, employee:c_schemas.EmployeeUpdate):
    db_employee=db.query(b_models.Employee).filter(b_models.Employee.id==emp_id).first()
    if db_employee :
        db_employee.name=employee.name
        db_employee.email=employee.email
        db.commit()
        db.refresh(db_employee)

    return db_employee

def delete_employee(db:Session,emp_id:int):
    db_employee=db.query(b_models.Employee).filter(b_models.Employee.id==emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee