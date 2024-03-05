from utils.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Double, ForeignKey
from sqlalchemy.orm import relationship


class FoodProduct(Base):
    __tablename__ = 'food_products'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    content = Column(String(255), nullable=False)
    avg_cooking_time = Column(String(100), nullable=True)


class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, nullable=False)
    food_product_id = Column(Integer, ForeignKey("food_products.id"), index=True)
    price = Column(Double, nullable=False)
