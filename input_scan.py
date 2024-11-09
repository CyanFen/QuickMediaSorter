import os
from interface_image_display import set_image, clear_image


extensions = {".png", ".jpg", ".jpeg", ".gif"}
input_path = None


def input_scan(path):
    global extensions, input_path
    input_path = path
    
    # Iterate through files in path
    for filename in os.listdir(path):
        # Check if file is of the correct file type(s)
        if any(filename.lower().endswith(ext) for ext in extensions):
            # Return the full path to the file
                # Deal with a bunch of path formatting BS - FIX THIS???
            mixed_path = (os.path.join(path, filename)) # Path including mixed / \ 's
            norm_path = os.path.normpath(mixed_path) # Normalize path so all slashes are the same direction
            set_image(norm_path, filename)
            
            return
        else:
            clear_image()
            print ("Cleared image and reset")
    
    # Return none if no matching files are found
    return None