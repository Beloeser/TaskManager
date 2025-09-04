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
        
        scrollFrame = ScrollableFrame(self.parent)
        scrollFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        weekTasks = self.taskManager.getWeekTasks(self.app.weekOffset)
        for day, tasks in weekTasks.items():
            dayFrame = tk.Frame(scrollFrame.scrollableFrame, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
            dayFrame.pack(fill="x", pady=5, padx=10)
            
            tk.Label(dayFrame, text=day, font=("Arial", 12, "bold"), 
                    fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=10, pady=5)
            
            sortedTasks = sorted(tasks, key=lambda x: x.time)
            for task in sortedTasks:
                tk.Label(dayFrame, text=f"  {task.time} - {task.name}",
                        font=("Arial", 14, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(anchor="w", padx=20)