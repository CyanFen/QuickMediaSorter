from interface_image_display import image_display_frame, image_display_label, image_name_label, update_image_size

def set_image(path, name):
    global image_path, image_name, image_display_frame, image_display_label, image_name_label
    image_path = path
    image_name = name
    
    image_name_label.configure(text=image_name)
    
    update_image_size(None, image_display_frame, image_display_label, image_path, image_name)