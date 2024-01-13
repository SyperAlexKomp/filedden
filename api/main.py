from configparser import ConfigParser
from fastapi import FastAPI, Header, File, Query

config = ConfigParser()
config.read("api/config.ini")

app = FastAPI()


@app.get("/", description="Base function that doing nothing")
async def root():
    return {
        "message": "Use /docs for documentation",
        "info": {
            "version": config.get("INFO", 'version')
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
