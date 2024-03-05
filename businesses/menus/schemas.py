from pydantic import BaseModel, Field


class FoodSchema(BaseModel):
    name: str = Field(None, description='Food Name')
    content: str = Field(None, description='Meal Content')
    avg_cooking_time: str = Field(None, description='Average Cooking Time')


class FoodResponseSchema(FoodSchema):
    id: int


class MenuItemCreateSchema(BaseModel):
    food_product_id: int
    price: float


class MenuItemSchema(BaseModel):
    id: int
    food_product: FoodResponseSchema
    price: float
