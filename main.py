from fastapi import FastAPI
from businesses.tables import routers
from utils.database import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router)
