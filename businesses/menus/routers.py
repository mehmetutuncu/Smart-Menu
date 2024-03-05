from fastapi import APIRouter, Depends, status, responses, HTTPException
from typing import List
from businesses.menus import schemas, crud
from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/menus",
    tags=["menu api"],
    responses={404: {"detail": "Not found"}},
)


@router.post('/foods/', response_model=schemas.FoodSchema, status_code=status.HTTP_201_CREATED)
async def create_food(food: schemas.FoodSchema, db: Session = Depends(get_db)):
    return crud.create_food(db, food=food)


@router.get('/foods/', response_model=List[schemas.FoodSchema], status_code=status.HTTP_200_OK)
async def read_foods(db: Session = Depends(get_db)):
    return crud.read_foods(db)


@router.post('/menu_items/', response_model=schemas.MenuItemCreateSchema, status_code=status.HTTP_201_CREATED)
async def create_menu_item(menu_item: schemas.MenuItemCreateSchema, db: Session = Depends(get_db)):
    return crud.create_menu_item(db, menu_item=menu_item)


@router.get('/menu_items/', response_model=List[schemas.MenuItemSchema], status_code=status.HTTP_200_OK)
async def read_menu_items(db: Session = Depends(get_db)):
    return crud.read_menu_items(db)
