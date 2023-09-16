from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username : str
    password : str
    level : Union[str, None] = None

# http://127.0.0.1:8000/hi?name=tam&reply=1234
@app.get("/")
def read_root():
    return {"Hello": "API"}

@app.get("/hi")
def hi(name:str, reply: Union[str, None] = None):
    return {"Hi": name, "Reply" : reply}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/login/")
def login(user: User):
    return {"echo": user}