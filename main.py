from fastapi import FastAPI
from businesses import business_main
from utils.database import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(business_main.router)
