from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sahil'}}

@app.get('/about')
def about():
    return {'data':{'data':'about-page'}}