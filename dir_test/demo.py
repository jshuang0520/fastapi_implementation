# -*- coding: utf-8 -*-
from enum import Enum
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import configparser
from dir_test.config import get_settings
print(f'get_settings().db_url: {get_settings().db_url}')


# parse value from app.ini
config = configparser.ConfigParser()
config.read('app.ini')
# print(f"dict(config['uwsgi']): {dict(config['uwsgi'])}")
# {
#    'wsgi-file': 'demo.py',
#    'callable': 'app',
#    'http': ':8080',
#    'threads': '2',
#    'processes': '4',
#    'master': 'true',
#    'chmod-socket': '660',
#    'vacuum': 'true',
#    'die-on-term': 'true'
# }


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/endpoint1')
def getAdsData():
    return 'welcome to test'


if __name__ == "__main__":
    uvicorn.run(
        "demo:app",
        reload=True,
        workers=1,
        log_level="info",
        access_log=True,
        use_colors=True,
        )
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))


"""Reference: https://github.com/tiangolo/fastapi

- to start:
uvicorn demo:app --reload  # or use command: python3 -m uvicorn demo:app --reload
uvicorn demo:app --reload --workers 1 --host 0.0.0.0 --port 8080

- Check it
Open your browser at http://127.0.0.1:8080/items/5?q=somequery
You will see the JSON response as:
{"item_id": 5, "q": "somequery"}

- Interactive API docs
Now go to http://127.0.0.1:8000/docs
- Alternative API docs
And now, go to http://127.0.0.1:8000/redoc.


# uvicorn main:app --reload  # zsh: command not found: uvicorn  # https://stackoverflow.com/questions/59025891/uvicorn-is-not-working-when-called-from-the-terminal
"""