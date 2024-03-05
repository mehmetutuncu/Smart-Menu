from businesses.tables import schemas, crud
from fastapi import APIRouter, Depends, status, responses, HTTPException
from typing import List

from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/tables",
    tags=["table api"],
    responses={404: {"detail": "Not found"}},
)


@router.get('/', response_model=List[schemas.TableSchema])
async def read_tables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), capacity: int = 0):
    return crud.read_tables(db, skip=skip, limit=limit, capacity=capacity)


@router.post('/', response_model=schemas.TableSchema, status_code=status.HTTP_201_CREATED)
async def create_table(table: schemas.TableSchema, db: Session = Depends(get_db)):
    return crud.create_table(db=db, table=table)


@router.patch(path='/{table_id}/', response_model=schemas.TableSchema, status_code=status.HTTP_200_OK)
async def update_table(table: schemas.TableSchema, table_id: int = 0, db: Session = Depends(get_db)):
    if table_id == 0 or crud.get_table_instance(db, table_id) is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Table reference id is required or reference id is not valid.')
    return crud.update_table(db, instance_id=table_id, table=table)
