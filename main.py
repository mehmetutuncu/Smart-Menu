from fastapi import FastAPI
from businesses.tables import routers as table_routers
from businesses.menus import routers as menu_routers
from utils.database import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(table_routers.router)
app.include_router(menu_routers.router)
