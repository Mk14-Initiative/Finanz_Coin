
# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

import main_window

def einstellung_window(parent_window):

    if parent_window:

        parent_window.destroy()

    settings_window = tk.Tk()

    settings_window.title("Einstellungen")

    back_button = tk.Button(settings_window, text = "Zurück", command = lambda: main_window.start_window(settings_window))

    close_button = tk.Button(settings_window, text = "Schließen", command = settings_window.destroy)

    back_button.pack()

    close_button.pack()




    settings_window.mainloop()




    return
