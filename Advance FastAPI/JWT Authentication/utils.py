import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        raise ValueError('Password must be 72 bytes or shorter')
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')

fake_user_db={
    'johndoe':{
        'username':'johndoe',
        'hashed_password':hash_password('secret123')
    }
}

# get user username
def get_user(username:str):
    user=fake_user_db.get(username)
    return user


# password cerification
def  verify_password(plan_password, hashed_password):
    return bcrypt.checkpw(
        plan_password.encode('utf-8'),
        hashed_password.encode('utf-8'),
    )