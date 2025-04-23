#!/usr/bin/python3

from fastapi import FastAPI, Form
from typing import Annotated
""""Working with Fastapis"""

app = FastAPI() #initializing fastapi to app


@app.get("/") # a get request
def root():
    return {"Message: my first api endpoint"}


@app.post("/products") # a post request
def shoe():
    return{"Numbers of Item": 24, "Colour": "Black and White"}


@app.get("/about-me/{Name}") #a path parameter, after the "/about-me/{Name}", provide anything (name) as your path
def info(Name):
    return{f"Information about {Name}"}


@app.get() #a query parameter (note: after the domain name and the "/user-me/" add "?name= any name you choose")
def details(name):
    return{"Message": f"information about {name}"}

@app.post("/sign_up")    #a request body
def details(name:Annotated[str, Form()], email:Annotated[str, Form()], age:Annotated[int, Form()], password:Annotated[str, Form()]):
    return {"Message" : f"logged in successfully"}