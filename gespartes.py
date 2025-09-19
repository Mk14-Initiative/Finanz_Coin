
# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

import main_window

def gespartes_window(parent_window):

    if parent_window:

        parent_window.destroy()

    reserve_window = tk.Tk()

    reserve_window.title("Gespartes")


    back_button = tk.Button(reserve_window, text = "Zurück", command = lambda: main_window.start_window(reserve_window))

    close_button = tk.Button(reserve_window, text = "Schließen", command = reserve_window.destroy)


    back_button.pack()

    close_button.pack()







    reserve_window.mainloop()

    return



