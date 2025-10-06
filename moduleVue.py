import tkinter as tk
from tkinter import ttk
#from tkcalendar import Calendar

class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #Label Usager
        self.label = ttk.Label(self, text="Usager")
        self.label.grid(row=1, column=0)

        # Usager entry
        self.usager_var = tk.StringVar()
        self.usager_entry = ttk.Entry(self, textvariable=self.usager_var, width=30)
        self.usager_entry.grid(row=1, column=1, sticky=tk.NSEW)

        #Label mot de passe
        self.label = ttk.Label(self, text="Mot de passe")
        self.label.grid(row=2, column=0)

        # mot de passe entry
        self.motPasse_var = tk.StringVar()
        self.motPasse_entry = ttk.Entry(self, textvariable=self.motPasse_var, width=30, show="*")
        self.motPasse_entry.grid(row=2, column=1, sticky=tk.NSEW)

        #Label device id
        self.label = ttk.Label(self, text="Device ID")
        self.label.grid(row=3, column=0)

        # device id entry
        self.deviceId_var = tk.StringVar()
        self.deviceId_entry = ttk.Entry(self, textvariable=self.deviceId_var, width=10)
        self.deviceId_entry.grid(row=3, column=1, sticky=tk.NSEW)

        #Date entry
