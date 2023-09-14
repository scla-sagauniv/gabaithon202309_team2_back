from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import gensim
from dotenv import load_dotenv
import os
from os.path import join, dirname

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

model = gensim.models.KeyedVectors.load_word2vec_format(os.environ.get("MODEL_PATH"), binary=False)

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

class Attribute(BaseModel):
    attribute: str
    
def getAttribute(word: str) -> Attribute:
    return Attribute(attribute=model.most_similar(word)[0][0])

class Choiced(BaseModel):
    word:str
    attribute:str
    choiced:bool

class ResWord(BaseModel):
    word:str
def getResTword(word,attribute: str) -> ResWord:
    return ResWord(word=model.most_similar(positive=[word,attribute])[0][0])
def getResFword(word,attribute: str) -> ResWord:
    return ResWord(word=model.most_similar(positive=[word], negative=[attribute])[0][0])


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/word")
async def root1(word: Word):
    attr = getAttribute(word=word.word)
    return attr
@app.post("/choiced")
async def root2(choiced: Choiced):
    if choiced.choiced:
        word=getResFword(word=choiced.word,attribute=choiced.attribute)
    else:
        word=getResTword(word=choiced.word,attribute=choiced.attribute)
    return word