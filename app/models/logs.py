from datetime import date
import uuid
class Log: 
    def __init__(self, food_id):
        self._id = uuid.uuid4().hex
        self._food_id = food_id
        self._date = date.today().isoformat()

    def __str__(self):
        return f"Id: {self.id}, Date: {self.date}"
        
    @property
    def id(self):
        return self._id

    @property
    def food_id(self):
        return self._food_id
    
    @property
    def date(self):
        return self._date
