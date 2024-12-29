'''
for installing FastAPI:
    1 - first we should make virtual envrionemnt (using uv or pip)
    2 - pip install "fastapi[standard]"
for run project for dev or standard :
    dev : fastapi dev main.py
    standard : fastapi run main.py
'''
from  enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    # Thies is tmp/example of value validation.
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# First Steps
@app.get("/") # "Path" here refers to the last part of the URL starting from the first '/',for example : https://example.com/items/foo
async def root():
    ''' this is First function on python FastAPI, this is 'hello world'. '''
    return {"message" : "Hello World"}

# fastapi auto generate docs on '/docs' or '/redocs'
# openapi generate json schemas on '/openapi.json'

# When building APIs, you normally use these specific HTTP methods to perform a specific action.
# Normally you use:
#
#     POST: to create data.
#     GET: to read data.
#     PUT: to update data.
#     DELETE: to delete data.
# So, in OpenAPI, each of the HTTP methods is calle d an "operation".
# We are going to call them "operations" too.


@app.get("/items/{item_id}")
async def read_item(item_id : int):
    ''' The value of the path parameter item_id will be passed to your function as the argument item_id.
            So, if you run this example and go to http://127.0.0.1:8000/items/foo, you will see a response of :
                {"item_id":"foo"} '''
    return {"item_id": item_id}


@app.get("/items/")
async def read_item_in_Fake_db(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



# This function it only get values from ENUM that defined earlier and return something.
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# for more details, read here.
# https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths
# https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor
