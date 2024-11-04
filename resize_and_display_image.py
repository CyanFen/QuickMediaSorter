from PIL import Image, ImageTk

# Load the image
image_name = "sortmyballs.png"
image_path = "photo_2020-08-26_22-20-38.jpg"
image_pil = Image.open(image_path)
image_width, image_height = image_pil.size



# Function to resize the image to fit the label dimensions without clipping
def resize_image(frame_width, frame_height):
    # Calculate the new size while preserving the aspect ratio
    aspect_ratio = image_width / image_height
    if frame_width / aspect_ratio > image_height:
        new_width = int(frame_height * aspect_ratio)
        new_height = int(frame_height)
    else:
        new_width = int(frame_width)
        new_height = int(frame_width / aspect_ratio)

    # Resize and return new image
    return image_pil.resize((new_width, new_height), Image.ANTIALIAS)
    

# Bind the resize event to dynamically adjust the image size
def update_image_size(event, frame, label):
    # Get current dimensions the image display frame
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    
    # Resize the image and update the label
    resized_image = resize_image(frame_width, frame_height)
    tk_image = ImageTk.PhotoImage(resized_image)
    label.configure(image=tk_image)
    label.image = tk_image
    