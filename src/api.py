from .app.storage import usage, versioning
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="KeyVaStoPy-API",
    description="API for KeyVaStoPy data interaction",
    version="0.1",
    servers=["127.0.0.1"]
)


@app.get('/')
def index():
    return {'message': 'Great Success!'}


@app.get('/use')
def use():
    return {
        'message': 'Great Success!',
        'usage': usage()
    }


@app.get('/ver')
def version():
    return {
        'message': 'Great Success!',
        'version': versioning()
    }


@app.get('/{key}')
def get_value_by_key():
    return {
        'message': 'Great Success!',
        'data': {}
    }


if __name__ == '__main__':
    uvicorn.run(app)
