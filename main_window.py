
# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

# Importiert die PhotoImage-Klasse für die Verwendung von Bildern
from tkinter import PhotoImage

import monats_uebersicht

import coin_variable

# Funktion zum Starten des Main window
def start_window(parent_window):

	# Überprüfen, ob ein übergeordnetes Fenster existiert
	if parent_window:

		# Wenn ja, das übergeordnete Fenster schließen
		parent_window.destroy()

	# Erstellen der Datenbanktabellen durch einen Aufruf an die chip-Instanz
	#chip.make_db_tabels()

	# Erstellen eines neuen Tkinter-Fensters
	main_window = tk.Tk()

	try:

		main_window.iconphoto(True, icon)  # Setzen des Icons für das Fenster

	except Exception as e:

		# Fehlerbehandlung, wenn das Laden des Icons fehlschlägt (z.B. wenn die Datei nicht gefunden wird)
		pass

	# Setzen des Titels für das Fenster
	main_window.title("Finanz Coin")

	main_window.minsize(200, 300)

	# Konfigurieren des Fensters mit den aus der chip-Instanz gelesenen Einstellungen
	#fc.config(bg=chip.read_row("settings", "bg")[0],  # Hintergrundfarbe
	#		  cursor=chip.read_row("settings", "cursor")[0],  # Cursorstil
	#		  relief=chip.read_row("settings", "relief")[0])  # Rahmenstil

	# Konfigurieren der Spalten und Zeilen im Tkinter-Fenster 'fc'

	# Spalte 0 konfigurieren:
	# Gewicht 1 bedeutet, dass die Spalte bei Bedarf wachsen kann,
	main_window.columnconfigure(0, weight=1)

	# Konfigurieren der Zeilen 1 bis 9:
	# Jede Zeile erhält ein Gewicht von 1, was bedeutet,
	# dass sie proportional zum verfügbaren Platz wachsen kann.
	main_window.rowconfigure(0, weight=1)  # Zeile 0 konfigurieren

	main_window.rowconfigure(1, weight=1)  # Zeile 1 konfigurieren

	main_window.rowconfigure(2, weight=1)  # Zeile 2 konfigurieren

	main_window.rowconfigure(3, weight=1)  # Zeile 3 konfigurieren

	main_window.rowconfigure(4, weight=1)  # Zeile 4 konfigurieren

	main_window.rowconfigure(5, weight=1)  # Zeile 5 konfigurieren

	main_window.rowconfigure(6, weight=1)  # Zeile 6 konfigurieren

	# Erstellen einer Schaltfläche "Monatsauswahl und Übersicht"
	monate_button = tk.Button(main_window, text="Monate Übersicht", command=lambda: monats_uebersicht.month_window(main_window))

	# Konfigurieren der Schaltfläche mit Hintergrundfarbe, Schriftfarbe, Schriftart und weiteren Eigenschaften
	#overview.config(bg=chip.read_row("settings", "bg")[0],   # Hintergrundfarbe
	#			fg=chip.read_row("settings", "fg")[0],   # Schriftfarbe
	#			font=(chip.read_row("settings", "font")[0],  # Schriftart
	#				  int(chip.read_row("settings", "font_size")[0]),  # Schriftgröße
	#				  chip.read_row("settings", "font_style")[0]),  # Schriftstil
	#			borderwidth=int(chip.read_row("settings", "borderwidth")[0]),  # Breite des Rahmens
	#			relief=chip.read_row("settings", "relief")[0],  # Reliefstil
	#			activebackground=chip.read_row("settings", "activebackground")[0],  # Hintergrundfarbe im aktiven Zustand
	#			cursor=chip.read_row("settings", "cursor")[0],  # Mauszeigerstil
	#			highlightthickness=chip.read_row("settings", "highlightthickness")[0],  # Dicke des Hervorhebungsrahmens
	#			highlightbackground=chip.read_row("settings", "highlightbackground")[0],  # Hintergrundfarbe des Hervorhebungsrahmens
	#			activeforeground=chip.read_row("settings", "activeforeground")[0])  # Schriftfarbe im aktiven Zustand

	# Erstellen einer Schaltfläche "Money Time"
	fixkosten_button = tk.Button(main_window, text="Fixkosten", command=lambda: x)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	#money_time.config(bg=chip.read_row("settings", "bg")[0],
	#			  fg=chip.read_row("settings", "fg")[0],
	#			  font=(chip.read_row("settings", "font")[0],
	#					int(chip.read_row("settings", "font_size")[0]),
	#					chip.read_row("settings", "font_style")[0]),
	#			  borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#			  relief=chip.read_row("settings", "relief")[0],
	#			  activebackground=chip.read_row("settings", "activebackground")[0],
	#			  cursor=chip.read_row("settings", "cursor")[0],
	#			  highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#			  highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#			  activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Reserve money View"
	gespartes_button = tk.Button(main_window, text="Gespartes Übersicht", command=lambda: x)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	#reserve_bar.config(bg=chip.read_row("settings", "bg")[0],
	#			   fg=chip.read_row("settings", "fg")[0],
	#			   font=(chip.read_row("settings", "font")[0],
	#					 int(chip.read_row("settings", "font_size")[0]),
	#					 chip.read_row("settings", "font_style")[0]),
	#			   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#			   relief=chip.read_row("settings", "relief")[0],
	#			   activebackground=chip.read_row("settings", "activebackground")[0],
	#			   cursor=chip.read_row("settings", "cursor")[0],
	#			   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#			   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#			   activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Statistic"
	statistik_button = tk.Button(main_window, text="Statistik", command=lambda: x)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften wie zuvor
	#statistics.config(bg=chip.read_row("settings", "bg")[0],
	#			  fg=chip.read_row("settings", "fg")[0],
	#			  font=(chip.read_row("settings", "font")[0],
	#					int(chip.read_row("settings", "font_size")[0]),
	#					chip.read_row("settings", "font_style")[0]),
	#			  borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#			  relief=chip.read_row("settings", "relief")[0],
	#			  activebackground=chip.read_row("settings", "activebackground")[0],
	#			  cursor=chip.read_row("settings", "cursor")[0],
	#			  highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#			  highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#			  activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Settings"
	settings_button = tk.Button(main_window, text="Einstellungen", command=lambda: x)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	#settings_button.config(bg=chip.read_row("settings", "bg")[0],
	#				   fg=chip.read_row("settings", "fg")[0],
	##				   font=(chip.read_row("settings", "font")[0],
	#						 int(chip.read_row("settings", "font_size")[0]),
	#						 chip.read_row("settings", "font_style")[0]),
	#				   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#				   relief=chip.read_row("settings", "relief")[0],
	#				   activebackground=chip.read_row("settings", "activebackground")[0],
	#				   cursor=chip.read_row("settings", "cursor")[0],
	#				   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#				   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#				   activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Help"
	help_button = tk.Button(main_window, text="Hilfe", command=lambda: x)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften wie zuvor
	#help_button.config(bg=chip.read_row("settings", "bg")[0],
	#			   fg=chip.read_row("settings", "fg")[0],
	#			   font=(chip.read_row("settings", "font")[0],
	#					 int(chip.read_row("settings", "font_size")[0]),
	#					 chip.read_row("settings", "font_style")[0]),
	#			   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#			   relief=chip.read_row("settings", "relief")[0],
	#			   activebackground=chip.read_row("settings", "activebackground")[0],
	#			   cursor=chip.read_row("settings", "cursor")[0],
	#			   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#			   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#			   activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Close"
	close_button = tk.Button(main_window, text="Schließen", command=main_window.destroy)

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	#close_button.config(bg=chip.read_row("settings", "bg")[0],
	#				fg=chip.read_row("settings", "fg")[0],
	#				font=(chip.read_row("settings", "font")[0],
	#					  int(chip.read_row("settings", "font_size")[0]),
	#					  chip.read_row("settings", "font_style")[0]),
	#				borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	#				relief=chip.read_row("settings", "relief")[0],
	#				activebackground=chip.read_row("settings", "activebackground")[0],
	#				cursor=chip.read_row("settings", "cursor")[0],
	#				highlightthickness=chip.read_row("settings", "highlightthickness")[0],
	#				highlightbackground=chip.read_row("settings", "highlightbackground")[0],
	#				activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Platzieren der Schaltfläche "Monatsauswahl und Übersicht" im Grid
	monate_button.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)  # Bei (0,0) positioniert, mit Padding

	# Platzieren der Schaltfläche "Fixkosten" im Grid
	fixkosten_button.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)  # Bei (0,2) positioniert, mit Padding

	# Platzieren der Schaltfläche "Reserve money View" im Grid
	gespartes_button.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)  # Bei (0,3) positioniert, mit Padding

	# Platzieren der Schaltfläche "Statistic" im Grid
	statistik_button.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)  # Bei (0,5) positioniert, mit Padding

	# Platzieren der Schaltfläche "Settings" im Grid
	settings_button.grid(column=0, row=4, sticky="nsew", padx=5, pady=5)  # Bei (0,7) positioniert, mit Padding

	# Platzieren der Schaltfläche "Help" im Grid
	help_button.grid(column=0, row=5, sticky="nsew", padx=5, pady=5)  # Bei (0,8) positioniert, mit Padding

	# Platzieren der Schaltfläche "Close" im Grid
	close_button.grid(column=0, row=6, sticky="nsew", padx=5, pady=5)  # Bei (0,9) positioniert, mit Padding

	# Starten der Hauptanwendungsschleife von Tkinter
	main_window.mainloop()

	# Rückgabe von der Funktion (da es keine Rückgabewerte gibt, ist dies optional)
	return
