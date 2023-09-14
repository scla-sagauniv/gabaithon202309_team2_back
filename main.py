from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Word(BaseModel):
    word: str

class Choiced(BaseModel):
    word:str
    attribute:str
    choiced:bool

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/word")
async def root1(word: Word):
    word.word = "res-" + word.word
    return word
@app.post("/choiced")
async def root2(word: Choiced):
    return word
async def root3(attribute: Choiced):
    return attribute
async def root4(choiced: Choiced):
    return choiced