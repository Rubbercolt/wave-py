import sqlite3

connection = sqlite3.connect('femi.db')

cursor = connection.cursor()




connection.close()