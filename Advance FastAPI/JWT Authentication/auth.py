from datetime import datetime, timedelta,timezone
from authlib.jose import JoseError, jwt
from fastapi import FastAPI, HTTPException


# Constatnts
SECRET_KEY='my_secret'
ALGORITHEM='HS256'
ACCESS_TOKEN_EXPIRY_MINUTES=30


# Function
def create_access_token(data:dict):
    header={'alg':ALGORITHEM}
    expire=datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    payload=data.copy()
    payload.update({'exp':expire})
    return jwt.encode(header,payload,SECRET_KEY)

# verify token
def verify_token(token:str):
    try :
        claims=jwt.decode(token, SECRET_KEY)
        claims.validate()
        username=claims.get('sub')
        if username is None:
            raise HTTPException(status_code=404, details='Token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=404, detail="Couldn't Validate Credentials")