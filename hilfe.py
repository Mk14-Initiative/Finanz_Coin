# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

import main_window

def hilfe_window(parent_window):

    if parent_window:

        parent_window.destroy()

    help_window = tk.Tk()

    help_window.title("Hilfe")

    back_button = tk.Button(help_window, text = "Zurück", command = lambda: main_window.start_window(help_window))

    close_button = tk.Button(help_window, text = "Schließen", command = help_window.destroy)

    back_button.pack()

    close_button.pack()



    help_window.mainloop()



    return
