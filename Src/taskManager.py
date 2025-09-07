from datetime import datetime, timedelta
from dataManager import DataManager
from task import RecurringTask, SporadicTask


class TaskManager:
    def __init__(self):
        self.dataManager = DataManager()
        self.recurringTasks = self.dataManager.loadRecurringTasks()
        self.sporadicTasks = self.dataManager.loadSporadicTasks()
        self.origins = self.dataManager.loadOrigins()
    
    def getTodayTasks(self):
        today = datetime.now()
        todayTasks = []
        
        # Recurring tasks for today
        for task in self.recurringTasks:
            if task.weekDay == today.weekday():
                todayTasks.append(task)
        
        # Sporadic tasks for today
        todayStr = today.strftime("%Y-%m-%d")
        for task in self.sporadicTasks:
            if task.date == todayStr and not task.completed:
                todayTasks.append(task)
        
        return sorted(todayTasks, key=lambda x: x.time)
    
    def getWeekTasks(self, weekOffset=0):
        today = datetime.now()
        startOfWeek = today + timedelta(weeks=weekOffset)
        weekTasks = {}
        
        for i in range(7):
            day = startOfWeek + timedelta(days=i)
            dayKey = f"{day.strftime('%A')} - {day.strftime('%d/%m')}"
            weekTasks[dayKey] = []
            
            # Recurring tasks
            for task in self.recurringTasks:
                if task.weekDay == day.weekday():
                    weekTasks[dayKey].append(task)
            
            # Sporadic tasks
            dayStr = day.strftime("%Y-%m-%d")
            for task in self.sporadicTasks:
                if task.date == dayStr and not task.completed:
                    weekTasks[dayKey].append(task)
        
        return weekTasks
    
    def getCompletedTasks(self):
        return [task for task in self.sporadicTasks if task.completed]
    
    def getTodoTasks(self):
        return [task for task in self.sporadicTasks if not task.completed]
    
    def getRecurringTasks(self):
        return self.recurringTasks
    
    def addSporadicTask(self, name, origin, date, time):
        task = SporadicTask(name, origin, date, time)
        self.sporadicTasks.append(task)
        self.dataManager.saveSporadicTasks(self.sporadicTasks)
    
    def addRecurringTask(self, name, origin, weekDay, time):
        task = RecurringTask(name, origin, weekDay, time)
        self.recurringTasks.append(task)
        self.dataManager.saveRecurringTasks(self.recurringTasks)
    
    def completeTask(self, task):
        task.completed = True
        self.dataManager.saveSporadicTasks(self.sporadicTasks)
    
    def deleteTask(self, task):
        if task in self.sporadicTasks:
            self.sporadicTasks.remove(task)
            self.dataManager.saveSporadicTasks(self.sporadicTasks)
        elif task in self.recurringTasks:
            self.recurringTasks.remove(task)
            self.dataManager.saveRecurringTasks(self.recurringTasks)