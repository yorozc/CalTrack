from models.food import Food
from models.logs import Log

class Service: # used by interface to create and manipulate data
    def __init__(self):
        self.foods = {}
        self.logs = {}

    def create_food(self, name: str, calories: float):
        new_food = Food(name, calories)
        self.foods[new_food.id] = new_food
        return new_food
