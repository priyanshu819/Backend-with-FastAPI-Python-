import bcrypt
from jose import jwt

SECRATE_KEY="my-super-secrate-key"
ALGORITHEM="HS256"

# create function to create token
def create_access_token(data:dict):
    return jwt.encode(
        data,
        SECRATE_KEY,
        algorithm=ALGORITHEM
    )

def hash_pas(password:str):
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')


def verify_password(password: str,hashed_password:str):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

