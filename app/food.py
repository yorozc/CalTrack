import uuid
class Food:
    def __init__(self, food_name, calories):
        self._id = uuid.uuid4().hex
        self.food_name = food_name
        self.calories = calories