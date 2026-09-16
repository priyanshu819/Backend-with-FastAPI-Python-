from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return("massage: Hello World")

@app.get("/about")
def about():
    return("massage: Algo Tantra is an Education h Platform where u can Learn AI")