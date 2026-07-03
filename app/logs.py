from datetime import date
import uuid
class Log: 
    def __init__(self, food_id):
        self._food_id = food_id
        self._date = date.today().isoformat()

    @property
    def food_id(self):
        return self._food_id
    
    @property
    def date(self):
        return self._date
