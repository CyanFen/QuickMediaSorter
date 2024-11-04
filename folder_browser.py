from tkinter import filedialog


input_path = None


# button will pass what button it should reference to set data, type will be used to determine the title of the file browser
def folder_browse(button, text, input):
    global input_path
    folder = filedialog.askdirectory(title=text)
    
    if folder:
        if input == True:
            input_path = folder
            return input_path
        else:
            button.configure(text=folder)
            
        
    
    
    
    #button.configure(text=folder)
    
