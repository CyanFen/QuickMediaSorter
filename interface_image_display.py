import customtkinter as ctk
from resize_and_display_image import image_name, image_path, update_image_size
import button_binding

app = None
master_frame = None

image_name_label = None
image_display_label = None
image_display_frame = None



def create_app():
    global app
    # Main interface container
    app = ctk.CTk()
    app.title("Quick Images Sorter")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.after(0, lambda: app.state('zoomed'))
    app.bind("<KeyPress>", button_binding.on_key_press)

    create_master_frame(app)
    
    return app

def create_master_frame(app):
    global master_frame
    # Full window frame
    master_frame = ctk.CTkFrame(app)
    master_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    master_frame.grid_columnconfigure(0, weight=1)
    master_frame.grid_rowconfigure(1, weight=1)
    
    create_image_display_elements(master_frame)
    
    return master_frame


def create_image_display_elements(master_frame):
    global image_name_label, image_display_frame, image_display_label
    # Image name frame
    image_name_frame = ctk.CTkFrame(master_frame)
    image_name_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    image_name_frame.grid_columnconfigure(0, weight=1) #image_name_label

    # Image name label
    image_name_label = ctk.CTkLabel(image_name_frame, text="Select a folder on the right to get started", font=("arial", 16))
    image_name_label.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")



    # Image display frame
    image_display_frame = ctk.CTkFrame(master_frame)
    image_display_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
    image_display_frame.grid_columnconfigure(0, weight=1) #image_display_label
    image_display_frame.grid_rowconfigure(0, weight=1) #image_display_label


    # Display image in image_display_frame using a label
    image_display_label = ctk.CTkLabel(image_display_frame, text="", font=("arial", 16))
    image_display_label.grid(column=0, row=0, sticky="nsew", padx=0, pady=0)

    # Bind the configure event to the image_display_frame to update the image size on resize
    image_display_frame.bind("<Configure>",lambda event: update_image_size(event, image_display_frame, image_display_label, image_path, image_name))
    
    
def set_image(path, name):
    global image_path, image_name, image_display_frame, image_display_label, image_name_label
    image_path = path
    image_name = name
    
    image_name_label.configure(text=image_name)
    
    update_image_size(None, image_display_frame, image_display_label, image_path, image_name)



# Run the app
if __name__ == "__main__":
    app = create_app()
    app.mainloop()


