from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to SHL API"}

@app.get("/do")
def do_something():
    return {"message": "This is the /do endpoint"}
