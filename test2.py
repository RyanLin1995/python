import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'msg': 'hello world'}


if __name__ == '__main__':
    uvicorn.run("test2:app", host='0.0.0.0', port=8001)
