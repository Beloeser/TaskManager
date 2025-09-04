import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors
from widgets.scrollFrame import ScrollableFrame

class TodayPage:
    def __init__(self, parent, taskManager):
        self.parent = parent
        self.taskManager = taskManager
    
    def show(self):
        tk.Label(self.parent, text="Tarefas de Hoje", 
                font=("Arial", 16, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=10)
        
        scrollFrame = ScrollableFrame(self.parent)
        scrollFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        todayTasks = sorted(self.taskManager.getTodayTasks(), key=lambda x: x.time)
        for task in todayTasks:
            frame = tk.Frame(scrollFrame.scrollableFrame, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
            frame.pack(fill="x", pady=5, padx=10)
            
            tk.Label(frame, text=f"{task.time} - {task.name} | {task.origin.name}",
                    font=("Arial", 12), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(side="left", padx=10, pady=5)