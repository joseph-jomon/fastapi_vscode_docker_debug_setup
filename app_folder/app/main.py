from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI



app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)



@app.get("/")
def read_root():
    myvar = "somvar"
    return {"Hello": f"World, its me{myvar} again Joseph with fast reload and launch debug config it is not attatch"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}