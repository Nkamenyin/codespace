#!/usr/bin/python3

from fastapi import FastAPI, Form, Path, Query, Header, Cookie, UploadFile, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel
import jwt


""""
This is a demo of my Working with Fastapis
"""

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


@app.get("/about-me") #a query parameter (note: after the domain name and the "/user-me/" add "?name= any name you choose")
def details(name):
    return{"Message": f"information about {name}"}


 #type casting in query parameter, adding other
#pydations like str, query, min and max lemth

@app.get("/about")
def details(name:Annotated[str, Query(min_length=2,max_length=14)]):
    return{"Message": f"information about {name}"}


@app.post("/sign_in")    #a form data
def details(name:Annotated[str, Form()], email:Annotated[str, Form()], age:Annotated[int, Form()], password:Annotated[str, Form()]):
    return {"Message" : f"logged in successfully"}

#creating a class that inherites from basemodel
#to be used in the request body

#also, creating a dictionary to be used in postman
""" {
        "name": "Val",
        "email":"val@gmail.com",
        "age":"89",
        "password":"12345"
    }
"""
class User(BaseModel):
    name:str
    email:str
    age:int
    password:int


@app.post("/sign_up/") #request body
def person(registration:User):
    return {"Status": "Sucess"}

#Headers
@app.get("/edit-post") 
def item(authorization: Annotated[str, Header()]):
    return {"user": f"{authorization}"}

#cookies
@app.get("/delete") 
def item(state: Annotated[str, Cookie()]):
    return {"user": f"{state}"}

#form data
@app.post("/lms_dashboard") 
def login(email: Annotated[str, Form()], password: Annotated[int, Form()], picture:UploadFile):
    return {"Status": "Successful", "email": f"{email}", "password": f"{password}","picture": f"{picture.filename}"}


#dependencies

def dependencies_1():
    result = 10 + 10
    return result


@app.get("/me")
def root(result=Depends(dependencies_1)):
    final = result + 90 - 13
    return {"Message": "Our first api endpoint", "final result":final}

#error handling
