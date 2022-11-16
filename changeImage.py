#!/usr/bin/env python3

# module imports
import os
from PIL import Image

# variables
user = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images'.format(user)

for image in image_directory:
    if 'tiff' in image:
        file_name = os.path.splitext(image)[0]
        new_file = image_directory + file_name + ".jpg"
        try:
            Image.open(new_file).convert("RGB").resize((600, 400)).save(new_file, "JPEG")
        except IOError:
            print("cannot convert", image)
