import sqlite3
import customtkinter as ctk

# sqlite3 connection and cursor
connection = sqlite3.connect("buttons.db")
cursor = connection.cursor()


def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buttons (
            id INTEGER PRIMARY KEY,
            binding_button INTEGER,
            path_button INTEGER,
            binding TEXT,
            path TEXT
        )
    ''')

def configure_binding(button, char):
    cursor.execute('UPDATE buttons SET binding = ? WHERE binding_button = ?', (char, id(button)))
    # Debug - print out buttons.db
    cursor.execute("SELECT * FROM buttons")

    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, binding_button: {row[1]}, path_button: {row[2]}, binding: {row[3]}, path: {row[4]}")  
    # End debug
    
def reset_binding(button):
    cursor.execute('UPDATE buttons SET binding = ? WHERE binding_button = ?', (None, id(button)))
    

def configure_path(button, path):
    cursor.execute('UPDATE buttons SET path = ? WHERE path_button = ?', (path, id(button)))
    # Debug - print out buttons.db
    cursor.execute("SELECT * FROM buttons")

    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, binding_button: {row[1]}, path_button: {row[2]}, binding: {row[3]}, path: {row[4]}")  
    # End debug

def reset_path(button):
    cursor.execute('UPDATE buttons SET path = ? WHERE path_button = ?', (None, id(button)))
    
def check_binding(char):
    cursor.execute('SELECT path FROM buttons WHERE binding = ?', (char))
    path = cursor.fetchone()
    if path:
        path = path[0]
    return path