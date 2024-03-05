from businesses.tables.models import Table
from businesses.tables.schemas import TableSchema
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_table_instance(db: Session, instance_id: int):
    return db.query(Table).filter(Table.id == instance_id).first()


def read_tables(db: Session, skip: int = 0, limit: int = 100, capacity: int = 0):
    if capacity == 0:
        qs = Table.capacity >= capacity
    else:
        qs = Table.capacity == capacity
    return db.query(Table).order_by(Table.floor, Table.number, Table.capacity).filter(qs).offset(skip).limit(
        limit).all()


def create_table(db: Session, table: TableSchema):
    last_table_instance = db.query(Table).order_by(desc(Table.id)).first()
    if last_table_instance:
        last_number = last_table_instance.number + 1
    else:
        last_number = 1
    table_instance = Table(name=table.name, floor=table.floor, is_reserved=table.is_reserved, capacity=table.capacity,
                           number=last_number)
    db.add(table_instance)
    db.commit()
    db.refresh(table_instance)
    return table_instance


def update_table(db: Session, instance_id: int, table: TableSchema):
    instance = get_table_instance(db, instance_id)
    for field, value in table.dict(exclude_unset=True).items():
        setattr(instance, field, value)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


