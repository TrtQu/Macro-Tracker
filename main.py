from fastapi import FastAPI

app = FastAPI()


foodDict = {
    'food': ['chicken', 'beef', '']
}

@app.get("/food")
def read_root():
    return {"message": "Hello World"}
