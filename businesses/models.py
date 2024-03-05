from utils.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, nullable=False)
    number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    is_reserved = Column(Boolean, default=False)
    capacity = Column(Integer, default=4)

