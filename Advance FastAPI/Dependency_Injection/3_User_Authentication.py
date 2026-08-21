from fastapi import FastAPI, Depends,Form,HTTPException,status
from fastapi.security import OAuth2PasswordBearer


app=FastAPI()
oauth2_schema=OAuth2PasswordBearer(tokenUrl='token')

@app.get('/')
def home():
    return 'Welcome In Priyanshu Softwere Solution !'

@app.post('/token')
def login(username:str=Form(..., ),password:str=Form(...,)):
    if username=='john' and password =='pass123':
        return{'access_token':'valid_token', 'token_type':'bearer'}
    raise HTTPException(status_code=404,detail='Invalid Credintials')

def decode_token(token:str):
    if  token=='valid_token':
        return {'name':'john'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Authenticatio Credentials')

def get_current_user(token:str=Depends(oauth2_schema)):
    return decode_token(token)

@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {"usernam":user['name']}

