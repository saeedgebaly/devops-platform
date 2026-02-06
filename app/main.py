from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DevOps Platform API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/env")
def env():
    return {
        "env": dict(os.environ)
    }
