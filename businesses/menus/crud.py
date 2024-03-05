from businesses.menus.models import MenuItem, FoodProduct
from businesses.menus.schemas import FoodSchema, MenuItemSchema, MenuItemCreateSchema
from sqlalchemy.orm import Session, contains_eager


def create_food(db: Session, food: FoodSchema):
    instance = FoodProduct(name=food.name, content=food.content,
                           avg_cooking_time=food.avg_cooking_time)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def read_foods(db: Session):
    return db.query(FoodProduct).order_by(FoodProduct.id).all()


def read_menu_items(db: Session):
    instances = db.query(MenuItem, FoodProduct).join(target=FoodProduct,
                                                     onclause=MenuItem.food_product_id == FoodProduct.id).all()
    return [{**menuitem.__dict__, 'food_product': foodproduct.__dict__} for menuitem, foodproduct in instances]


def create_menu_item(db: Session, menu_item: MenuItemCreateSchema):
    instance = MenuItem(food_product=menu_item.food_product, price=menu_item.price)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
