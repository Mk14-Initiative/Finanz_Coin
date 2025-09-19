# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

import main_window

def fixkosten_window(parent_window):

    if parent_window:

        parent_window.destroy()


    fixcost_window = tk.Tk()

    fixcost_window.title("Fixkosten")


    back_button = tk.Button(fixcost_window, text = "Zurück", command = lambda: main_window.start_window(fixcost_window))


    close_button = tk.Button(fixcost_window, text = "Schließen", command = fixcost_window.destroy)

    back_button.pack()

    close_button.pack()











    fixcost_window.mainloop()


    return


