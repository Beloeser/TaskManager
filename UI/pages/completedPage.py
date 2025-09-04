import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors
from widgets.scrollFrame import ScrollableFrame

class CompletedPage:
    def __init__(self, parent, taskManager, app):
        self.parent = parent
        self.taskManager = taskManager
        self.app = app
        self.checkVars = []
    
    def show(self):
        tk.Label(self.parent, text="Tarefas Concluídas", 
                font=("Arial", 16, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=10)
        
        scrollFrame = ScrollableFrame(self.parent)
        scrollFrame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        completedTasks = sorted(self.taskManager.getCompletedTasks(), key=lambda x: (x.date, x.time))
        self.checkVars = []
        
        for task in completedTasks:
            frame = tk.Frame(scrollFrame.scrollableFrame, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
            frame.pack(fill="x", pady=2, padx=10)
            
            var = tk.BooleanVar()
            self.checkVars.append((var, task))
            chk = tk.Checkbutton(frame, variable=var, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY,
                               selectcolor=Colors.BG_SECONDARY, activebackground=Colors.BG_TERTIARY)
            chk.pack(side="left", padx=5)
            
            tk.Label(frame, text=f"{task.name} - {task.date} {task.time}",
                    font=("Arial", 10), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(side="left", padx=5, pady=5)
        
        tk.Button(self.parent, text="APAGAR SELECIONADAS", 
                 bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY, font=("Arial", 10, "bold"),
                 command=self.deleteSelected).pack(pady=10)
    
    def deleteSelected(self):
        for var, task in self.checkVars:
            if var.get():
                self.taskManager.deleteTask(task)
        self.app.showCompleted()