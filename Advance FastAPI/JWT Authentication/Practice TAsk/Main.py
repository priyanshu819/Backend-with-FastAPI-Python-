from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr
from Security import hash_pas ,verify_password

app=FastAPI()

# Create A PydanticMOdel for Registration
class User(BaseModel):
    username:str
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
    hashed_pass=hash_pas(user.password)
    fake_db[user.username]={
        "username":user.username,
        "email":user.email,
        "password":hashed_pass
    }
    
    return {'message':'User Got Regesterd SucssesFully !'}

# Create A PydanticMOdel for Registration
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
    return f"Hey {user.username} Login SuccessFully"