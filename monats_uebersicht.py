import tkinter as tk

from tkinter import ttk

from tkinter import *

from tkinter import colorchooser

import datetime

import main_window

def month_window(parent_window):

    if parent_window:

        parent_window.destroy()

    monats_window = tk.Tk()

    monats_window.title("Monatsübersicht")

    monats_window.minsize(200, 300)

    #monats_window.config( left config)

    monats_window.columnconfigure(0, weight = 1)

    monats_window.columnconfigure(1, weight = 1)

    monats_window.columnconfigure(2, weight = 1)

    monats_window.columnconfigure(3, weight = 1)

    monats_window.columnconfigure(4, weight = 1)

    monats_window.rowconfigure(0, weight = 1)

    monats_window.rowconfigure(1, weight = 1)

    monats_window.rowconfigure(2, weight = 1)

    back_button = tk.Button(monats_window, text = "Zurück", command =lambda:main_window.start_window(monats_window))

    year_label = tk.Label(monats_window, text = "Jahr")

    month_label = tk.Label(monats_window, text = "Monat")

    new_month_label = tk.Label(monats_window, text = "Neuer Monat")

    delete_month_label = tk.Label(monats_window, text = "Monat Löschen")

    sync_labe = tk.Label(monats_window, text = "Sync")

    back_button.grid(column = 0, row = 1, sticky = "nsew")

    year_label.grid(column = 0, row = 0, sticky = "nsew")

    month_label.grid(column = 1, row = 0, sticky = "nsew")

    new_month_label.grid(column = 2, row = 0, sticky = "nsew")

    delete_month_label.grid(column = 3, row = 0, sticky = "nsew")

    sync_labe.grid(column = 4, row = 0, sticky = "nsew")

    close_button = tk.Button(monats_window, text="Schließen", command=monats_window.destroy)

    close_button.grid(column = 0, row = 2, sticky = "nsew")


    monats_window.mainloop()

    return































