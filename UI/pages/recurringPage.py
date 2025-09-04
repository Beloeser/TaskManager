import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors

class RecurringPage:
    def __init__(self, parent, taskManager, app):
        self.parent = parent
        self.taskManager = taskManager
        self.app = app
    
    def show(self):
        tk.Label(self.parent, text="Tarefas Recorrentes por Dia da Semana", 
                font=("Arial", 16, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=10)
        
        # Create main frame for columns
        columnsFrame = tk.Frame(self.parent, bg=Colors.BG_PRIMARY)
        columnsFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        weekDays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        recurringTasks = self.taskManager.getRecurringTasks()
        
        # Group tasks by weekday and sort by time
        tasksByDay = {i: [] for i in range(7)}
        for task in recurringTasks:
            tasksByDay[task.weekDay].append(task)
        
        # Sort tasks by time for each day
        for day in tasksByDay:
            tasksByDay[day] = sorted(tasksByDay[day], key=lambda x: x.time)
        
        # Create columns for each day
        for dayIndex, dayName in enumerate(weekDays):
            dayColumn = tk.Frame(columnsFrame, bg=Colors.BG_SECONDARY, relief="solid", bd=1)
            dayColumn.pack(side="left", fill="both", expand=True, padx=2)
            
            # Day header
            tk.Label(dayColumn, text=dayName, font=("Arial", 12, "bold"), 
                    bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY).pack(fill="x", pady=2)
            
            # Tasks for this day
            for task in tasksByDay[dayIndex]:
                taskFrame = tk.Frame(dayColumn, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
                taskFrame.pack(fill="x", padx=5, pady=2)
                
                tk.Label(taskFrame, text=f"{task.time}", font=("Arial", 9, "bold"), 
                        fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=5)
                tk.Label(taskFrame, text=task.name, font=("Arial", 8), 
                        fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY, wraplength=100).pack(anchor="w", padx=5)
                tk.Label(taskFrame, text=task.origin.name, font=("Arial", 7), 
                        fg=Colors.TEXT_SECONDARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=5)
                
                tk.Button(taskFrame, text="EXCLUIR", bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY, 
                         font=("Arial", 7), command=lambda t=task: self.deleteTask(t)).pack(pady=2)
    
    def deleteTask(self, task):
        self.taskManager.deleteTask(task)
        self.app.showRecurring()