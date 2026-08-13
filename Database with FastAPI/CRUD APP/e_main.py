from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from a_database import engine, sessionlocal,base
from typing import List
import b_models,c_schemas,d_crud


base.metadata.create_all(bind=engine)

app=FastAPI()

# dependency with the database
