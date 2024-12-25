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
