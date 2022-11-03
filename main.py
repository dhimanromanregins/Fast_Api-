from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Blog-list'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':{'data':'Unpublished Blogs'}}

@app.get('/blog/{id}')
def about(id:int):
    # fetch blog with id = id
    return {'data':{'data':id}}


@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{'1', '2'}}


