from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr,field_validator,Field
from Security import hash_pas ,verify_password
import re

app=FastAPI()

# Create A PydanticMOdel for Registration
class User(BaseModel):
    username:str=Field(...,  description="use only a-z, 0-9 and underscore _ ") 
    fullname:str
    email:EmailStr
    password:str

# Create a fake db
fake_db={}


# Create a home api
@app.get('/')
def home():
    return "Welcome in Priyanshu Tiwari Softwere World !"

#create Register Api
@app.post('/register')
def register(user:User):

    # create condition for uniqueness of the email and username
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="username alredy exist")
    for existEmail in fake_db.values():
        if existEmail['email']==user.email:
            raise HTTPException(status_code=400, detail="email alredy exist")

    # set the credintials of the username
    pattern=r"^[a-z0-9_]+$"
    if not re.match(pattern,user.username) or not (3<=len(user.username)<=20):
        raise HTTPException(status_code=422, detail="use only a-z, 0-9 and underscore _ in username")

    hashed_pass=hash_pas(user.password)
    fake_db[user.username]={
        "username":user.username,
        "fullname":user.fullname,
        "email":user.email,
        "password":hashed_pass
    }
    
    return {'message':'User Got Regesterd SucssesFully !'}

# Create A PydanticMOdel for login
class User(BaseModel):
    
    username:str
    password:str


# Create Api For LogIN
@app.post('/login')
def login(user:User):

    stored_user=fake_db.get(user.username)

    if not stored_user:
        raise HTTPException(status_code=401, detail="User not Found !")
    check_password=verify_password(user.password,stored_user['password'])
    if not check_password:
        raise HTTPException(status_code=401, detail="Invalid Password !")
    return f"Hey {stored_user['fullname']} Login SuccessFully"