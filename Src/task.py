from datetime import datetime
from origin import Origin

class Task:
    def __init__(self, name, origin, completed=False):
        self.name = name
        self.origin = origin
        self.completed = completed
    
    def toDict(self):
        return {
            "name": self.name,
            "origin": self.origin.toDict(),
            "completed": self.completed
        }

class RecurringTask(Task):
    def __init__(self, name, origin, weekDay, time, completed=False):
        super().__init__(name, origin, completed)
        self.weekDay = weekDay  # 0-6 (Monday to Sunday)
        self.time = time  # format "HH:MM"
    
    def toDict(self):
        data = super().toDict()
        data.update({
            "type": "recurring",
            "weekDay": self.weekDay,
            "time": self.time
        })
        return data
    
    @classmethod
    def fromDict(cls, data):
        origin = Origin.fromDict(data["origin"])
        return cls(data["name"], origin, data["weekDay"], data["time"], data.get("completed", False))

class SporadicTask(Task):
    def __init__(self, name, origin, date, time, completed=False):
        super().__init__(name, origin, completed)
        self.date = date  # format "YYYY-MM-DD"
        self.time = time  # format "HH:MM"
    
    def toDict(self):
        data = super().toDict()
        data.update({
            "type": "sporadic",
            "date": self.date,
            "time": self.time
        })
        return data
    
    @classmethod
    def fromDict(cls, data):
        origin = Origin.fromDict(data["origin"])
        return cls(data["name"], origin, data["date"], data["time"], data.get("completed", False))