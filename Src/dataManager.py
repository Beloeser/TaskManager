import json
import os
from task import RecurringTask, SporadicTask
from origin import Origin

class DataManager:
    def __init__(self):
        self.dbPath = "../DB"
        self.recurringTasksFile = os.path.join(self.dbPath, "recurringTasks.json")
        self.sporadicTasksFile = os.path.join(self.dbPath, "sporadicTasks.json")
        self.originsFile = os.path.join(self.dbPath, "origins.json")
    
    def saveRecurringTasks(self, tasks):
        data = [task.toDict() for task in tasks]
        with open(self.recurringTasksFile, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def loadRecurringTasks(self):
        if not os.path.exists(self.recurringTasksFile):
            return []
        with open(self.recurringTasksFile, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [RecurringTask.fromDict(item) for item in data]
    
    def saveSporadicTasks(self, tasks):
        data = [task.toDict() for task in tasks]
        with open(self.sporadicTasksFile, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def loadSporadicTasks(self):
        if not os.path.exists(self.sporadicTasksFile):
            return []
        with open(self.sporadicTasksFile, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [SporadicTask.fromDict(item) for item in data]
    
    def saveOrigins(self, origins):
        data = [origin.toDict() for origin in origins]
        with open(self.originsFile, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def loadOrigins(self):
        if not os.path.exists(self.originsFile):
            return []
        with open(self.originsFile, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Origin.fromDict(item) for item in data]