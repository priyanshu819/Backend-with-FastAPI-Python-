from fastapi import FastAPI,Depends

app=FastAPI()

class Settings:
    def __init__(self):
        self.api_key='my_secrate'
        self.debug=True

# create dependencies function
def get_Settings():
    return Settings()

@app.get('/config')
def getConfig(settings:Settings=Depends(get_Settings)):  # Dependeny Injection
    return {'api_key':settings.api_key}