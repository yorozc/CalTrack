from models.food import Food
from models.logs import Log
import datetime

class Service: # used by interface to create and manipulate data
    def __init__(self):
        self.foods = {}
        self.logs = {}

    def create_food(self, name: str, calories: float):
        new_food = Food(name, calories)
        self.foods[new_food.id] = new_food
        return new_food

    def create_log(self, food_id):
        if food_id not in self.foods.keys():
            return "Food does not exist!"
        new_log = Log(food_id)
        self.logs[new_log.id] = new_log
        return new_log