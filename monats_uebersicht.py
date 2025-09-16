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

    close_button = tk.Button(monats_window, text="Schließen", command=monats_window.destroy)

    close_button.pack()


    monats_window.mainloop()

    return































