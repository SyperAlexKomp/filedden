from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="Base function that doing nothing")
async def root():
    return {"message": "use /docs for documentation"}

# TODO
@app.post("/load")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
