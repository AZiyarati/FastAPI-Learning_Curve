'''
for installing FastAPI:
    1 - first we should make virtual envrionemnt (using uv or pip)
    2 - pip install "fastapi[standard]"
for run project for dev or standard :
    dev : fastapi dev main.py
    standard : fastapi run main.py
'''
from fastapi import FastAPI

app = FastAPI()


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
