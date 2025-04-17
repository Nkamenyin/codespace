#!/usr/bin/python3

from fastapi import FastAPI
""""Working with Fastapis"""

app = FastAPI() #initializing fastapi to app

@app.get(/)
    def root():
        return {"Message: my first api endpoint"}

