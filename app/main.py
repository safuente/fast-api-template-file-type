from fastapi import FastAPI

app = FastAPI()

ALLOWED_HOSTS=['*']

@app.get("/")
async def root():
    return {"message": "Hello World"}