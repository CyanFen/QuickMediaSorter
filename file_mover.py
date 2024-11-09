import resize_and_display_image as radi
import shutil

def move(target_path):
    try:
        shutil.move(radi.image_path, target_path)
    except FileExistsError:
        duplicate = radi.image_path + " (1)"
        shutil.move(duplicate, target_path)