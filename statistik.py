
# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

import main_window

def statistik_window(parent_window):

    if parent_window:

        parent_window.destroy()

    statistic_window = tk.Tk()

    statistic_window.title("Statistik")


    back_button = tk.Button(statistic_window, text = "Zurück", command = lambda: main_window.start_window(statistic_window))

    close_button = tk.Button(statistic_window, text = "Schließen", command = statistic_window.destroy)

    back_button.pack()

    close_button.pack()


    statistic_window.mainloop()






    return

