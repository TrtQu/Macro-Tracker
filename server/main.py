from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Category(Enum):
    MEAL = "meal"
    INGREDIENT = "ingredient"

class Food(BaseModel):
    name: str
    calories: int
    protein: int
    category: Category

foods = {
    0: Food(name="Chicken", calories=50, protein=43, category=Category.INGREDIENT),
    1: Food(name="Ground Beef", calories=40, protein=50, category=Category.INGREDIENT),
}

@app.get("/food/{food_id}")
def read_root(food_id: int) -> Food:
    if food_id not in foods:
        raise HTTPException(
            status_code=404, detail=f"Item with {food_id=} does not exist"
        )
    return foods[food_id]
