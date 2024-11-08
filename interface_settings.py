import customtkinter as ctk
from interface_image_display import app, master_frame
import folder_browser
import button_click_handler
from sqlite_module import cursor

input_folder = None

remember_settings = False

keybind_count = 6 # Number of keybinds to add
row_counter = 0 # Incremented value when a new row is added up to keybind_count

def select_input_folder(target_folder_button, target_folder_label):
    global input_folder
    input_folder = folder_browser.folder_browse(target_folder_button, "Select folder to sort images...", True)
    target_folder_label.configure(text=input_folder)

def add_settings():
    settings_frame = ctk.CTkFrame(master_frame, width=300)
    settings_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
    settings_frame.grid_propagate(False)
    settings_frame.grid_columnconfigure(0, weight=1)
    
    target_folder_label = ctk.CTkLabel(settings_frame, text=input_folder, font=("arial", 16))
    target_folder_label.grid(column=0, row=1, padx=20)
    
    target_folder_button = ctk.CTkButton(settings_frame, text="Select Folder to Sort", font=("arial", 16), command=lambda: select_input_folder(target_folder_button, target_folder_label))
    target_folder_button.grid(column=0, row=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
    
    destinations_frame = ctk.CTkFrame(settings_frame)
    destinations_frame.grid(column=0, row=2, sticky="nsew", padx=(10,10), pady=20)
    
    create_binding_row(destinations_frame)
    
    return settings_frame



def create_binding_row(destinations_frame):
    global keybind_count, row_counter
    
    if remember_settings == False:
        cursor.execute('''DELETE FROM buttons''')
    
    while row_counter < keybind_count:
        destination_binding_button = ctk.CTkButton(destinations_frame, height=30, width=30, text="")
        destination_binding_button.grid(column=0, row=row_counter, padx=(10,10), pady=20)
        destination_binding_button.configure(command=lambda button=destination_binding_button: button_click_handler.button_clicked(button))
        
        destination_browse_button = ctk.CTkButton(destinations_frame, text="Select folder to bind", font=("arial", 16))
        destination_browse_button.grid(column=1, row=row_counter, padx=(0,20), pady=20, sticky="w")
        destination_browse_button.configure(command=lambda button=destination_browse_button: button_click_handler.button_clicked(button))
        
        button_click_handler.binding_dictionary[id(destination_binding_button)] = destination_binding_button
        button_click_handler.path_dictionary[id(destination_browse_button)] = destination_browse_button
        
        
        # Assign relevent values to a list to feed into buttons.db
        values = (row_counter, id(destination_binding_button), id(destination_browse_button), None, None)
    
        cursor.execute('''
            INSERT INTO buttons (id, binding_button, path_button, binding, path)
            VALUES (?, ?, ?, ?, ?)
        ''', values)  

        # Increment row_counter for next loop step
        row_counter += 1
    
    # Debug - print out buttons.db
    cursor.execute("SELECT * FROM buttons")

    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, binding_button: {row[1]}, path_button: {row[2]}, binding: {row[3]}, path: {row[4]}")  
    # End debug
    
            
# Run the app
if __name__ == "__main__":
    settings_frame = add_settings()
    settings_frame.mainloop()
    
    