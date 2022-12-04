from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def graph2(city_i, city_d):
    testRoute = ["Kephallonia", "Melos", "Hydrea", "Argolis"]
    return testRoute

@app.get("/graph")
async def read_item(city_i: str, city_d: str):
    final = graph2(city_i, city_d)
    return final
