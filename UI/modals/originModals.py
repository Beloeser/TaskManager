import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors

class AddOriginModal:
    def __init__(self, parent, taskManager, callback):
        self.parent = parent
        self.taskManager = taskManager
        self.callback = callback
        
        self.window = tk.Toplevel(parent)
        self.window.title("Adicionar Origem")
        self.window.geometry("300x150")
        self.window.configure(bg=Colors.BG_PRIMARY)
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setupUI()
    
    def setupUI(self):
        tk.Label(self.window, text="Nova Origem", font=("Arial", 14, "bold"), 
                fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=20)
        
        tk.Label(self.window, text="Nome:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack()
        self.nameEntry = tk.Entry(self.window, width=30, bg=Colors.BG_TERTIARY, 
                                 fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.nameEntry.pack(pady=10)
        self.nameEntry.bind('<Return>', lambda e: self.addOrigin())
        self.nameEntry.focus_set()
        
        buttonFrame = tk.Frame(self.window, bg=Colors.BG_PRIMARY)
        buttonFrame.pack(pady=20)
        
        tk.Button(buttonFrame, text="ADICIONAR", bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 10, "bold"), command=self.addOrigin).pack(side="left", padx=10)
        
        tk.Button(buttonFrame, text="CANCELAR", bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 10, "bold"), command=self.window.destroy).pack(side="left", padx=10)
    
    def addOrigin(self):
        name = self.nameEntry.get().strip()
        if name:
            sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'Src'))
            from origin import Origin
            origin = Origin(name)
            origins = self.taskManager.dataManager.loadOrigins()
            origins.append(origin)
            self.taskManager.dataManager.saveOrigins(origins)
            self.callback()
            self.window.destroy()

class DeleteOriginModal:
    def __init__(self, parent, taskManager, callback):
        self.parent = parent
        self.taskManager = taskManager
        self.callback = callback
        
        self.window = tk.Toplevel(parent)
        self.window.title("Excluir Origem")
        self.window.geometry("300x200")
        self.window.configure(bg=Colors.BG_PRIMARY)
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setupUI()
    
    def setupUI(self):
        tk.Label(self.window, text="Excluir Origem", font=("Arial", 14, "bold"), 
                fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack(pady=20)
        
        origins = self.taskManager.dataManager.loadOrigins()
        if not origins:
            tk.Label(self.window, text="Nenhuma origem cadastrada", 
                    fg=Colors.TEXT_SECONDARY, bg=Colors.BG_PRIMARY).pack(pady=20)
            return
        
        tk.Label(self.window, text="Selecione a origem:", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_PRIMARY).pack()
        
        self.originVar = tk.StringVar()
        originCombo = ttk.Combobox(self.window, textvariable=self.originVar, width=25,
                                  values=[origin.name for origin in origins])
        originCombo.pack(pady=10)
        
        buttonFrame = tk.Frame(self.window, bg=Colors.BG_PRIMARY)
        buttonFrame.pack(pady=20)
        
        tk.Button(buttonFrame, text="EXCLUIR", bg=Colors.DANGER, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 10, "bold"), command=self.deleteOrigin).pack(side="left", padx=10)
        
        tk.Button(buttonFrame, text="CANCELAR", bg=Colors.ACCENT, fg=Colors.TEXT_PRIMARY,
                 font=("Arial", 10, "bold"), command=self.window.destroy).pack(side="left", padx=10)
    
    def deleteOrigin(self):
        selectedName = self.originVar.get()
        if selectedName:
            origins = self.taskManager.dataManager.loadOrigins()
            origins = [origin for origin in origins if origin.name != selectedName]
            self.taskManager.dataManager.saveOrigins(origins)
            self.callback()
            self.window.destroy()