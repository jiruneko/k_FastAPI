from fastapi import FastAPI

app = FastAPI()

@app.get('/blog/category')
def category():
  return {'data': 'all category'}

@app.get('/blog/{id}')
def show(id:int):
  return {'data': id}

@app.get('blog/{id}/comments')
def comments(id):
  return {'data': {id, comments}}
