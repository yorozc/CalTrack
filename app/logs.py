from datetime import date
import uuid
class Log: 
    def __init__(self, food_id):
        self.food_id = food_id
        self.date = date.today().isoformat()

