
import sqlite3

import os

from contextlib import closing

from os.path import exists

import datetime

curren_path = os.getcwd()

db_path = curren_path + "/" + "coin.db"

year_dic = {1: "January", 2: "February", 3: "March", 4: "April", 5: "Mai", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

#
# make db
#
def make_db():

	exists_db = exists(db_path)

	if exists_db == False:

		with closing(sqlite3.connect(db_path)) as db:

			with closing(db.cursor()) as cu:
			
				pass

			return

	return

#
# read specifed table
#
def read_dbtable(table):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			read_table = f"SELECT ID, Outgo, Sume FROM {table}"

			in_table = cu.execute(read_table).fetchall()

			return in_table

	return

#
# dlete specified db line
#
def delete_dbline(table, row):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:
		
			read_row = f"DELETE From {table} WHERE ID = {row}"

			cu.execute(read_row)

			db.commit()

			return

	return

#
# delete table
#
def delete_table(value):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			del_table = f"DROP TABLE IF EXISTS {value}"

			cu.execute(del_table)

			db.commit()

	return

#
# get last line
#
def get_lastline(table):

	with closing(sqlite3.connect(db_path)) as db:
	
		with closing(db.cursor()) as cu:
	
			cu.execute(f"SELECT * FROM {table} ORDER BY ROWID DESC LIMIT 1")

			last_line = cu.fetchone()

		return last_line

	return

#
# update db line
#
def update_dbrowline(table, update):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO {table}(outgo, sume) VALUES(?, ?)"

			cu.execute(update_row, update)

			db.commit()

	return

#
# make main outgo table
#
def make_moneytime():

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			cu.execute("CREATE TABLE IF NOT EXISTS money_time(ID INTEGER PRIMARY KEY AUTOINCREMENT, outgo Text NOT Null, sume FLOAT NOT Null, time Text NOT NULL, endtime Text Not NULL)")

			db.commit()

			return

#
# update db line
#
def update_dbline(table, update):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_line = f"UPDATE {table} SET outgo = ?, sume = ? WHERE id = ?"

			cu.execute(update_line, (update[1], update[2], update[0]))

			db.commit()

		return

#
# get all tables
#
def read_tables():

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			cu.execute("SELECT name FROM sqlite_master WHERE type = 'table'; ")

			tabels = cu.fetchall()

			return [tabels[0] for tabels in tabels]

#
# change line money_time line
#
def change_moneytimerow(update):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_row = f"UPDATE money_time SET outgo = ?, sume = ?, time = ?, endtime = ? WHERE id = ?"

			cu.execute(update_row, (update[1], update[2], update[3], update[4], update[0]))

			db.commit()

	return

#
# add line money_time
#
def add_moneytimerow(update):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO money_time (outgo, sume, time, endtime) VALUES(?, ?, ?, ?)"

			cu.execute(update_row, update)

			db.commit()

	return

#
# read table money_time
#
def read_moneytimetable():

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			read_table = f"SELECT id, outgo, sume, time, endtime FROM money_time"

			in_table = cu.execute(read_table).fetchall()

			return in_table

	return

#
# make initial_moneytime_table
#
def initial_moneytime_table():

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO money_time (outgo, sume, time, endtime) VALUES('first', 1.0, 'month', 'none')"

			cu.execute(update_row)

			db.commit()

	return

#
# make new month table with out primary key
#
def new_monthtable(table):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			new_table = f"CREATE TABLE IF NOT EXISTS {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT, outgo Text NOT Null, sume FLOAT NOT Null)"

			cu.execute(new_table)

			db.commit()

			return

	return

#
# add row monnth table
#
def add_row(table, row):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"ALTER TABLE {table} ADD COLUMN {row} TEXT")

			db.commit()

	return

#
# change specified row
#
def change_row(table, row, value):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update = (f"UPDATE {table} SET {row} = ? WHERE ID = 0")

			cu.execute(update, (value,))

			db.commit()

	return

#
# update initial_settings_table
#
def initial_settings_table(table):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO {table} (ID) VALUES (0)"

			cu.execute(update_row)

			db.commit()

	return

#
# make initial_settings_table
#
def make_settings_table(table):

	with closing(sqlite3.connect(db_path)) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"CREATE TABLE IF NOT EXISTS {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT)")

			db.commit()

			return

	return

#
# insert row
#
def insert_row(table, row, value):

	with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"INSERT INTO {table} (ID, {row}) VALUES (?, ?)",(0, value))

			db.commit()

	return

#
# make list from tubple
#
def make_list_fromtuple(value):

	return list(value)

#
# make list from tuple
#
# make list from tuple
def make_list(value):

	return [list(item) for item in value]

#
# get first line
#
def get_firsttable_line(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			query = f"SELECT * FROM {table} LIMIT 1"

			cu.execute(query)

			first_row = cu.fetchone()

			return first_row

	return

#
# check if table exist
#
def table_exist(tablename):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute("SELECT name FROM sqlite_master WHERE type='table' AND name =?", (tablename,),)

			result = cu.fetchone()

			return result

	return

#
# make primary key table
#
def primary_keytable(value):

	new_list = []

	for i in value:

		for j in i:

			new_list.append(j[0])

	return new_list

#
# check or make tabel at programm start
#
def make_db_tabels():

	make_db()

	result = table_exist("money_time")

	if result is None:

		make_moneytime()

		initial_moneytime_table()

	result = table_exist("settings")

	if result is None:

		make_settings_table("settings")

		initial_settings_table("settings")

		style_row = ["bg", "fg", "font", "font_size", "font_style", "borderwidth", "relief", "activebackground", 
		"cursor", "highlightthickness", "highlightbackground", "activeforeground", "window_visible"]

		standart_values = ["#ffffff", "#000000", "Arial", 10, "normal", 1, "flat", "#ffffff", "arrow", 1, "#000000", "#000000", 100]

		for i in style_row:

			add_row("settings", i)

		for i, j in zip(style_row, standart_values):

			change_row("settings", i, j)
		
	return









