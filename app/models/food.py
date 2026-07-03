import uuid
class Food:
    def __init__(self, food_name, calories):
        self._id = uuid.uuid4().hex
        self._food_name = food_name
        self._calories = calories
    
    @property
    def id(self):
        return self._id
    
    @property
    def food_name(self):
        return self._food_name
    
    @food_name.setter
    def food_name(self, val):
        self._food_name = val

    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, val):
        self._calories = val