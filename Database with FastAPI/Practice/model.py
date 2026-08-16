from sqlalchemy import Column, Integer, String
from Database import base

class Employee(base):
    __tablename__='employes'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    email=Column(String, unique=True, index=True)

