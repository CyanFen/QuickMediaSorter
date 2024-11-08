from tkinter import filedialog
import sqlite_module


active_button = None
binding_dictionary = {}
path_dictionary = {}


def button_clicked(button):
    global active_button
    
    # Binding button
    if button in binding_dictionary.values():
        active_button = button
        button.configure(text="")
    
    # Folder button    
    if button in path_dictionary.values():
        active_button = None
        set_path(button)  
                     
def set_binding(event):
    global active_button
    
    # Capitalize given character if it is lowercase
    if active_button: #refers to the button object
        char = event.char.upper() if event.char.islower() else event.char  # Capitalize if lowercase
        
        if binding_dictionary:
            # Loop through all buttons to ensure no other button has the same key bound
            for btn in binding_dictionary.values():
                if btn.cget("text") == char:
                    btn.configure(text="")
                    sqlite_module.reset_binding(btn)
                
        # Set the character on the active button
        active_button.configure(text=char)
        sqlite_module.configure_binding(active_button, char)
        active_button = None
        
    
def set_path(button):
    path = filedialog.askdirectory(title="Select folder to bind key to...")
    
    for pth in path_dictionary.values():
        if pth.cget("text") == path:
            pth.configure(text="Select folder to bind")
            sqlite_module.reset_path(pth)
    
    if path:
        button.configure(text=path)
        sqlite_module.configure_path(button, path)
        
        