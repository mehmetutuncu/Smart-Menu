from pydantic import BaseModel, Field


class TableSchema(BaseModel):
    floor: int = Field(default=None, description='It contains information on '
                                                 'which floor the table is located on.')
    name: str = Field(default='', description='Descriptive name.')
    is_reserved: bool = Field(default=False, description='Reservation status.')
    capacity: int = Field(default=4, description='Capacity of the table', gt=1, lt=7)
