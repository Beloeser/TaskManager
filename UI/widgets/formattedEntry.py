import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors

class DateWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=Colors.BG_SECONDARY, **kwargs)
        
        self.dayEntry = tk.Entry(self, width=4, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.dayEntry.pack(side="left", padx=2)
        
        tk.Label(self, text="/", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).pack(side="left")
        
        self.monthEntry = tk.Entry(self, width=4, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.monthEntry.pack(side="left", padx=2)
        
        tk.Label(self, text="/", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY).pack(side="left")
        
        self.yearEntry = tk.Entry(self, width=6, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.yearEntry.pack(side="left", padx=2)
    
    def getValue(self):
        day = self.dayEntry.get().zfill(2)
        month = self.monthEntry.get().zfill(2)
        year = self.yearEntry.get().zfill(4)
        return f"{year}-{month}-{day}"

class TimeWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=Colors.BG_SECONDARY, **kwargs)
        
        self.hourEntry = tk.Entry(self, width=4, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.hourEntry.pack(side="left", padx=2)
        
        tk.Label(self, text=":", fg=Colors.TEXT_PRIMARY, bg=Colors.BG_SECONDARY, font=("Arial", 12, "bold")).pack(side="left")
        
        self.minuteEntry = tk.Entry(self, width=4, bg=Colors.BG_TERTIARY, fg=Colors.TEXT_PRIMARY, insertbackground=Colors.TEXT_PRIMARY)
        self.minuteEntry.pack(side="left", padx=2)
    
    def getValue(self):
        hour = self.hourEntry.get().zfill(2)
        minute = self.minuteEntry.get().zfill(2)
        return f"{hour}:{minute}"