import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from colors import Colors

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self, bg=Colors.BG_PRIMARY, highlightthickness=0)
        
        # Configure scrollbar style
        style = ttk.Style()
        style.configure("Vertical.TScrollbar", 
                       background=Colors.BG_SECONDARY,
                       troughcolor=Colors.BG_TERTIARY,
                       bordercolor=Colors.BORDER,
                       arrowcolor=Colors.TEXT_SECONDARY,
                       darkcolor=Colors.BG_SECONDARY,
                       lightcolor=Colors.BG_SECONDARY)
        
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollableFrame = tk.Frame(self.canvas, bg=Colors.BG_PRIMARY)
        
        self.scrollableFrame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollableFrame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Bind canvas resize to update scrollable frame width
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollableFrame.bind("<MouseWheel>", self._on_mousewheel)
    
    def _on_canvas_configure(self, event):
        # Update the scrollable frame width to match canvas width
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")