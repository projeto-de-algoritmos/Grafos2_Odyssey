from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graphMainUse import cityGraphUCS

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/graph")
async def read_item(city_i: str, city_d: str):
    begin = city_i
    destiny = city_d    
    final = cityGraphUCS(begin, destiny)
    return final
