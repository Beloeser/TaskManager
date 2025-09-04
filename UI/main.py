import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Src'))

from taskManager import TaskManager
from pages.todayPage import TodayPage
from pages.calendarPage import CalendarPage
from pages.recurringPage import RecurringPage
from pages.completedPage import CompletedPage
from pages.todoPage import TodoPage
from pages.managePage import ManagePage
from colors import Colors

class TaskApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("800x600")
        
        self.taskManager = TaskManager()
        self.weekOffset = 0
        
        self.setupUI()
        
    def setupUI(self):
        self.root.configure(bg=Colors.BG_PRIMARY)
        
        # Header
        header = tk.Frame(self.root, bg=Colors.BG_SECONDARY, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        title = tk.Label(header, text="GERENCIADOR DE TAREFAS", 
                        font=("Arial", 18, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY)
        title.pack(pady=15)
        
        # Navigation
        nav = tk.Frame(self.root, bg=Colors.BG_TERTIARY, height=50)
        nav.pack(fill="x")
        nav.pack_propagate(False)
        
        buttons = [
            ("HOJE", self.showToday),
            ("CALENDÁRIO", self.showCalendar),
            ("RECORRENTES", self.showRecurring),
            ("FEITAS", self.showCompleted),
            ("A FAZER", self.showTodo),
            ("GERENCIAR", self.showManage)
        ]
        
        for text, command in buttons:
            btn = tk.Button(nav, text=text, command=command, 
                          bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY, font=("Arial", 10, "bold"),
                          relief="flat", padx=20, activebackground=Colors.ACCENT_HOVER)
            btn.pack(side="left", padx=5, pady=10)
        
        # Content area
        self.contentFrame = tk.Frame(self.root, bg=Colors.BG_PRIMARY)
        self.contentFrame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.showToday()
    
    def clearContent(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
    
    def showToday(self):
        self.clearContent()
        page = TodayPage(self.contentFrame, self.taskManager)
        page.show()
    
    def showCalendar(self):
        self.clearContent()
        page = CalendarPage(self.contentFrame, self.taskManager, self)
        page.show()
    
    def showRecurring(self):
        self.clearContent()
        page = RecurringPage(self.contentFrame, self.taskManager, self)
        page.show()
    
    def showCompleted(self):
        self.clearContent()
        page = CompletedPage(self.contentFrame, self.taskManager, self)
        page.show()
    
    def showTodo(self):
        self.clearContent()
        page = TodoPage(self.contentFrame, self.taskManager, self)
        page.show()
    
    def showManage(self):
        self.clearContent()
        page = ManagePage(self.contentFrame, self.taskManager, self)
        page.show()
    
    def previousWeek(self):
        self.weekOffset -= 1
        self.showCalendar()
    
    def nextWeek(self):
        self.weekOffset += 1
        self.showCalendar()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TaskApp()
    app.run()