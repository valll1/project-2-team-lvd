import sqlite3 # import neccesary libraries
import pandas as pd

def create_tables(): # defining the create_table function
  # creates the database
  db_conn = sqlite3.connect('sports_database.db')
  cursor = db_conn.cursor()
  # Stores the create table statements into one list
  tables = ['''
      CREATE TABLE mens_volleyball (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          height FLOAT not NULL
      )''',
          '''CREATE TABLE womens_volleyball (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          height FLOAT not NULL
      )''',
            '''CREATE TABLE mens_swimming_diving (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          height FLOAT not NULL
      )''',
            '''CREATE TABLE womens_swimming_diving (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          height FLOAT not NULL
      )''']
  # loops through the list, executing and commiting changes
  for table in tables:
    cursor.execute(table)
    db_conn.commit()
# defines the inter_values function that takes the csv-filled dictionary as a parameter
def insert_values(csv_dict):
  create_tables() # runs the create_table, creating the tables before values are inserted
  # iterates through the csv-filled dictionary
  for csv, team_name in csv_dict.items():
    df = pd.read_csv(csv) # reads csv and turns it into a dataframe
    if team_name == 'Mens Volleyball': # matches team name to specific table for insertion
      value = tuple(df.values) # turn a single row into a tuple for insertion
      cursor.executemany("INSERT INTO mens_volleyball(name, height) VALUES (?, ?)", value) #inserts into specific table

    elif team_name == 'Womens Volleyball':
      value = tuple(df.values)
      cursor.executemany("INSERT INTO womens_volleyball(name, height) VALUES (?, ?)", value)

    elif team_name == 'Mens Swimming Diving':
      value = tuple(df.values)
      cursor.executemany("INSERT INTO mens_swimming_diving(name, height) VALUES (?, ?)", value)

    else:
      value = tuple(df.values)
      cursor.executemany("INSERT INTO womens_swimming_diving(name, height) VALUES (?, ?)", value)
    #commits changes
    db_conn.commit()
    #closes database
    db_conn.close()
