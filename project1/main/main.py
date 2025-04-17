#!/usr/bin/python3

from fastapi import FastAPI
""""Working with Fastapis"""

app = FastAPI() #initializing fastapi to app

@app.get("/") # a get request
def root():
    return {"Message: my first api endpoint"}

@app.post("/products") # a post request
def shoe():
    return{"Numbers of Item": 24, "Colour": "Black and White"}