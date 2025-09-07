import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors
from widgets.scrollFrame import ScrollableFrame

class CalendarPage:
    def __init__(self, parent, taskManager, app):
        self.parent = parent
        self.taskManager = taskManager
        self.app = app
    
    def show(self):
        # Header with navigation
        headerFrame = tk.Frame(self.parent, bg=Colors.BG_PRIMARY)
        headerFrame.pack(pady=10)
        
        tk.Button(headerFrame, text="◀ Semana Anterior", command=self.app.previousWeek,
                 bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY, font=("Arial", 10, "bold"),
                 activebackground=Colors.ACCENT_HOVER).pack(side="left", padx=10)
        
        tk.Label(headerFrame, text="Calendário Semanal", 
                font=("Arial", 16, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(side="left", padx=20)
        
        tk.Button(headerFrame, text="Próxima Semana ▶", command=self.app.nextWeek,
                 bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY, font=("Arial", 10, "bold"),
                 activebackground=Colors.ACCENT_HOVER).pack(side="left", padx=10)
        
        # Create main frame for columns
        columnsFrame = tk.Frame(self.parent, bg=Colors.BG_PRIMARY)
        columnsFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        weekTasks = self.taskManager.getWeekTasks(self.app.weekOffset)
        
        # Create columns for each day
        for dayKey, tasks in weekTasks.items():
            dayColumn = tk.Frame(columnsFrame, bg=Colors.BG_SECONDARY, relief="solid", bd=1)
            dayColumn.pack(side="left", fill="both", expand=True, padx=2)
            
            # Day header with date
            tk.Label(dayColumn, text=dayKey, font=("Arial", 12, "bold"), 
                    bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY).pack(fill="x", pady=2)
            
            # Tasks for this day
            if tasks:
                sortedTasks = sorted(tasks, key=lambda x: x.time)
                for task in sortedTasks:
                    taskFrame = tk.Frame(dayColumn, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
                    taskFrame.pack(fill="x", padx=5, pady=2)
                    
                    tk.Label(taskFrame, text=f"{task.time}", font=("Arial", 9, "bold"), 
                            fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=5)
                    tk.Label(taskFrame, text=task.name, font=("Arial", 8), 
                            fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY, wraplength=100).pack(anchor="w", padx=5)
                    if hasattr(task, 'origin'):
                        tk.Label(taskFrame, text=task.origin.name, font=("Arial", 7), 
                                fg=Colors.TEXT_SECONDARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=5)