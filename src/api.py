from .app.storage import usage, versioning
from fastapi import FastAPI

app = FastAPI('')


@app.get('/')
async def index():
    return {'message': 'Great Success!'}


@app.get('/use')
async def use():
    return {
        'message': 'Great Success!',
        'usage': usage()
    }


@app.get('/ver')
async def version():
    return {
        'message': 'Great Success!',
        'version': versioning()
    }


@app.get('/{key}')
async def get_value_by_key():
    return {
        'message': 'Great Success!',
        'data': {value}
    }