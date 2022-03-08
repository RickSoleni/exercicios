from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item_id}')
async def root(item_id: int):
    soma = item_id * 10
    return soma


@app.put('/')
async def pentakill():
    return 'pentakill'
