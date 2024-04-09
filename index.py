from fastapi import FastAPI
from routes.studentRoutes import studentApp

# Creates a new FastAPI application instance
app = FastAPI()

#  Router calls studentApp into your FastAPI application
app.include_router(studentApp)
