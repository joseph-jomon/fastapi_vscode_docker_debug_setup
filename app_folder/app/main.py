from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates




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

# Mount the static directory to serve static files like CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the directory where your templates are stored
templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        name="item.html",  # The name of the template file
        context={"request": request, "id": id}  # Context data to be passed to the template
    )

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str):
    # Process the search query (for now, we'll just pass it back to the template)
    return templates.TemplateResponse(
        "search_results.html",  # A new template we'll create
        {"request": request, "query": query}
    )



@app.get("/")
def read_root():
    myvar = "somvar"
    return {"Hello": f"World, its me{myvar} again Joseph with fast reload and launch debug config it is not attatch"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}