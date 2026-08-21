from fastapi import FastAPI, Depends

app= FastAPI()

# define dependency function
def get_db():
    db={'connection':'mock_db_connection'}
    try:
        yield db
    finally:
        db.close()

# endpoint
@app.get('/home')
def home(db=Depends(get_db)):
    return {'db_status':db['connection']}