import os
from interface_image_display import set_image

extensions = {".png", ".jpg", ".jpeg", ".gif"}



def input_scan(path):
    global extensions, image_path, image_name
    
    # Iterate through files in path
    for filename in os.listdir(path):
        # Check if file is of the correct file type(s)
        if any(filename.lower().endswith(ext) for ext in extensions):
            # Return the full path to the file
            set_image((os.path.join(path, filename)), filename)
            return
    
    # Return none if no matching files are found
    return None
    
    