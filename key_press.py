import button_click_handler
import file_mover
import sqlite_module




def key_pressed(event):
    # If binding button is awaiting input, bind key to binding button
    if button_click_handler.active_button:
        button_click_handler.set_binding(event)
        return
    
    # Check if key pressed is bound, if it is attempt to move file to a given path (if there is one)
    char = event.char.upper() if event.char.islower() else event.char # Capitalize if lowercase
    
    path = sqlite_module.check_binding(char)
    # If path is not bound, ignore key press
    if path == None:
        return
    
    # if path is anything but None, move the file to the given path
    file_mover.move(path)
    
    from input_scan import input_scan, input_path
    input_scan(input_path)
