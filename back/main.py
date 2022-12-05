from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cityList import cityList
from primGraph import primGraph

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
    for city in cityList:
        if city[0] == city_i:
            begin = city[1]
        if city[0] == city_d:
            destiny == city[1]
        
    final = primGraph(begin, destiny)
    return final
