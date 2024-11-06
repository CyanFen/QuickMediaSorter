


binding_path_buttons_dictionary = {}
binding_dictionary = {}
path_dictionary = {}


def button_clicked(button):
    if button in binding_path_buttons_dictionary:
            print("BINDING BUTTON")
            # Update binding_buttons_dictionary
            binding_path_buttons_dictionary[char] = binding_path_buttons_dictionary.pop(active_button)
            print(binding_path_buttons_dictionary)
        
    if button in binding_path_buttons_dictionary.values():    
            print("PATH BUTTON")