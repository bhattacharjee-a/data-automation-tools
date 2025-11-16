import os
import shutil

def organize(folder):
    for file in os.listdir(folder):
        if '.' in file:
            ext = file.split('.')[-1]
            ext_folder = os.path.join(folder, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(folder, file), os.path.join(ext_folder, file))
