import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors
from widgets.formattedEntry import DateWidget, TimeWidget
from widgets.scrollFrame import ScrollableFrame


class ManagePage:
    def __init__(self, parent, taskManager, app):
        self.parent = parent
        self.taskManager = taskManager
        self.app = app
    
    def show(self):
        tk.Label(self.parent, text="Gerenciar Tarefas", 
                font=("Arial", 16, "bold"), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=10)
        
        # Create main scroll frame for entire page
        mainScrollFrame = ScrollableFrame(self.parent)
        mainScrollFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sporadic Tasks Section
        sporadicFrame = tk.LabelFrame(mainScrollFrame.scrollableFrame, text="Tarefas Esporádicas", 
                                    font=("Arial", 12, "bold"), fg=Colors.TEXT_PRIMARY, 
                                    bg=Colors.BG_SECONDARY, bd=1, relief="solid")
        sporadicFrame.pack(fill="x", pady=10, padx=10)
        
        # Add sporadic task form
        tk.Label(sporadicFrame, text="Nome:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.sporadicNameEntry = tk.Entry(sporadicFrame, width=20, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.sporadicNameEntry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(sporadicFrame, text="Origem:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.sporadicOriginVar = tk.StringVar()
        self.sporadicOriginCombo = ttk.Combobox(sporadicFrame, textvariable=self.sporadicOriginVar, width=12)
        self.sporadicOriginCombo.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(sporadicFrame, text="Data:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.sporadicDateEntry = DateWidget(sporadicFrame)
        self.sporadicDateEntry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(sporadicFrame, text="Hora:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.sporadicTimeEntry = TimeWidget(sporadicFrame)
        self.sporadicTimeEntry.grid(row=1, column=3, padx=5, pady=5)
        
        tk.Button(sporadicFrame, text="ADICIONAR", bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY, 
                 font=("Arial", 10, "bold"), activebackground=Colors.ACCENT_HOVER,
                 command=self.addSporadicTask).grid(row=2, column=1, pady=10)
        
        # Recurring Tasks Section
        recurringFrame = tk.LabelFrame(mainScrollFrame.scrollableFrame, text="Tarefas Recorrentes", 
                                     font=("Arial", 12, "bold"), fg=Colors.TEXT_PRIMARY,
                                     bg=Colors.BG_SECONDARY, bd=1, relief="solid")
        recurringFrame.pack(fill="x", pady=10, padx=10)
        
        # Add recurring task form
        tk.Label(recurringFrame, text="Nome:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.recurringNameEntry = tk.Entry(recurringFrame, width=20, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.recurringNameEntry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(recurringFrame, text="Origem:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.recurringOriginVar = tk.StringVar()
        self.recurringOriginCombo = ttk.Combobox(recurringFrame, textvariable=self.recurringOriginVar, width=12)
        self.recurringOriginCombo.grid(row=0, column=3, padx=5, pady=5)
        
        # Update origin combos after both are created
        self.updateOriginCombo()
        
        tk.Label(recurringFrame, text="Dia da Semana:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.weekDayVar = tk.StringVar(value="0")
        weekDayCombo = ttk.Combobox(recurringFrame, textvariable=self.weekDayVar, width=12,
                                   values=["0-Segunda", "1-Terça", "2-Quarta", "3-Quinta", "4-Sexta", "5-Sábado", "6-Domingo"])
        weekDayCombo.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(recurringFrame, text="Hora:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.recurringTimeEntry = TimeWidget(recurringFrame)
        self.recurringTimeEntry.grid(row=1, column=3, padx=5, pady=5)
        
        tk.Button(recurringFrame, text="ADICIONAR", bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY, 
                 font=("Arial", 10, "bold"), activebackground=Colors.ACCENT_HOVER,
                 command=self.addRecurringTask).grid(row=2, column=1, pady=10)
        
        # List existing recurring tasks
        listFrame = tk.Frame(recurringFrame, bg=Colors.BG_SECONDARY)
        listFrame.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
        
        recurringTasks = sorted(self.taskManager.getRecurringTasks(), key=lambda x: (x.weekDay, x.time))
        for task in recurringTasks:
            frame = tk.Frame(listFrame, bg=Colors.BG_TERTIARY, relief="solid", bd=1)
            frame.pack(fill="x", pady=2)
            
            weekDays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
            dayName = weekDays[task.weekDay]
            
            tk.Label(frame, text=f"{task.name} - {dayName} {task.time} | {task.origin.name}",
                    font=("Arial", 10), fg=Colors.TEXT_PRIMARY, bg=Colors.BG_TERTIARY).pack(side="left", padx=5, pady=5)
            
            tk.Button(frame, text="EXCLUIR", bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY, 
                     font=("Arial", 8), command=lambda t=task: self.deleteRecurringTask(t)).pack(side="right", padx=5, pady=2)
        
        # Origin management buttons
        originFrame = tk.Frame(mainScrollFrame.scrollableFrame, bg=Colors.BG_PRIMARY)
        originFrame.pack(pady=20)
        
        tk.Label(originFrame, text="Gerenciar Origens:", font=("Arial", 12, "bold"), 
                fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(side="left", padx=10)
        
        tk.Button(originFrame, text="+ NOVA ORIGEM", bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 9, "bold"), command=self.openAddOriginModal).pack(side="left", padx=5)
        
        tk.Button(originFrame, text="- EXCLUIR ORIGEM", bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 9, "bold"), command=self.openDeleteOriginModal).pack(side="left", padx=5)
    
    def updateOriginCombo(self):
        origins = self.taskManager.dataManager.loadOrigins()
        originNames = [origin.name for origin in origins]
        self.sporadicOriginCombo['values'] = originNames
        self.recurringOriginCombo['values'] = originNames
    
    def addSporadicTask(self):
        name = self.sporadicNameEntry.get()
        originName = self.sporadicOriginVar.get()
        date = self.sporadicDateEntry.getValue()
        time = self.sporadicTimeEntry.getValue()
        
        if name and originName and date and time:
            origins = self.taskManager.dataManager.loadOrigins()
            origin = next((o for o in origins if o.name == originName), None)
            if origin:
                self.taskManager.addSporadicTask(name, origin, date, time)
                self.app.showManage()
    
    def addRecurringTask(self):
        name = self.recurringNameEntry.get()
        originName = self.recurringOriginVar.get()
        weekDay = int(self.weekDayVar.get().split("-")[0])
        time = self.recurringTimeEntry.getValue()
        
        if name and originName and time:
            origins = self.taskManager.dataManager.loadOrigins()
            origin = next((o for o in origins if o.name == originName), None)
            if origin:
                self.taskManager.addRecurringTask(name, origin, weekDay, time)
                self.app.showManage()
    
    def deleteRecurringTask(self, task):
        self.taskManager.deleteTask(task)
        self.app.showManage()
    
    def openAddOriginModal(self):
        import importlib.util
        modal_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modals', 'originModals.py'))
        spec = importlib.util.spec_from_file_location("originModals", modal_path)
        originModals = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(originModals)
        originModals.AddOriginModal(self.parent, self.taskManager, self.refreshOrigins)
    
    def openDeleteOriginModal(self):
        import importlib.util
        modal_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modals', 'originModals.py'))
        spec = importlib.util.spec_from_file_location("originModals", modal_path)
        originModals = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(originModals)
        originModals.DeleteOriginModal(self.parent, self.taskManager, self.refreshOrigins)
    
    def refreshOrigins(self):
        self.updateOriginCombo()
        self.app.showManage()