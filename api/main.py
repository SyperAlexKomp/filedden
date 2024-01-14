from configparser import ConfigParser
from fastapi import FastAPI, Header, File, Query
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from api.database.repo import Repo

global_config = ConfigParser()
global_config.read("config.ini")

config = ConfigParser()
config.read("api/config.ini")

app = FastAPI()
repo = Repo()


@app.get("/", description="Base function that doing nothing")
async def root():
    return {
        "message": "Use /docs for documentation",
        "info": {
            "version": global_config.get("API", 'version')
        }
    }


# TODO
@app.post("/load")
async def load(api_key: str = Header(description="Your api key",
                                     title="Api Key"),
               file: bytes = File(description="File that you want to load",
                                  title="File"),
               file_name: str = Query(default=None,
                                      description="Name of your file. Will generate random if not provided",
                                      title="File Name")):
    return {"message": f"Hello"}


@app.on_event("startup")
async def startup():
    await repo.connect(host=config.get("DATABASE", 'host'),
                       user=config.get("DATABASE", 'user'),
                       password=config.get("DATABASE", 'password'),
                       database=config.get("DATABASE", 'database'))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)