import resize_and_display_image as radi
import shutil

def move(path):
    shutil.move(radi.image_path, path)