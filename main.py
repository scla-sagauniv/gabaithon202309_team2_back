from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('models/demo2.txt', binary=False)

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

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/word")
async def root1(word: Word):
    attr = getAttribute(word=word.word)
    return attr
@app.post("/choiced")
async def root2(choiced: Choiced):
    return choiced