active_button = None
bound_buttons = []

def on_button_click(button, frame):
    print("button clicked")
    global active_button
    button.configure(text="") # Clears the current text on button
    active_button = button # Set the active button variable
    frame.focus_set() # Set focus to capture keypress
    
def on_key_press(event):
    print("key pressed")
    global active_button
    
    # Capitalize given character if it is lowercase
    if active_button:
        char = event.char.upper() if event.char.islower() else event.char  # Capitalize if lowercase
        
        if bound_buttons:
            # Loop through all buttons to ensure no other button has the same key bound
            for btn in bound_buttons:
                if btn.cget("text") == char:
                    btn.configure(text="")
                
        # Set the character on the active button
        active_button.configure(text=char)
        active_button = None
        
        