from PIL import Image
import customtkinter as ctk


# Load the image
image_name = None
image_path = None





# Function to resize the image to fit the label dimensions without clipping
def resize_image(frame_width, frame_height):
    global image_path
    if image_path:
         # Open the image with PIL
        image_pil = Image.open(image_path)
        image_width, image_height = image_pil.size
        
        # Calculate scaling factors to fit image within frame dimensions
        width_ratio = frame_width / image_width
        height_ratio = frame_height / image_height
        scale_factor = min(width_ratio, height_ratio)  # Choose the smaller scale to avoid cropping

        # Calculate new dimensions based on scale factor
        new_width = int(image_width * scale_factor)
        new_height = int(image_height * scale_factor)
            
        # Resize the image using PIL
        resized_image = image_pil.resize((new_width, new_height), Image.ANTIALIAS)
        
        # Convert the resized PIL into a CTkImage for high DPI compatiblity
        ctk_image = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(new_width, new_height))
        return ctk_image
    

# Bind the resize event to dynamically adjust the image size
def update_image_size(event, frame, label, path, name):
    global image_path, image_name
    image_path = path
    image_name = name
    if image_path:
        
        # Get current dimensions of the image display frame
        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()
        
        # Resize the image and update the label
        ctk_image = resize_image(frame_width, frame_height)
        if ctk_image:
            label.configure(image=ctk_image)
            label.image = ctk_image
            print("Set image")
    