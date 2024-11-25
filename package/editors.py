# This file contains all the functions used by the main program
# to edit images.

from package.utils import load, save

# This is a list containing all the exportable functions of this file.
__all__ = [
    "mirror_horizontally",
    "mirror_vertically",
]

# This function mirrors an image horizontally.
def mirror_horizontally(old_image_path, new_image_path):
    # Opens the image and get it as a matrix.
    try:
        image = load(old_image_path)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Initial path error.")
    
    # Mirror it horizontally.
    for row in image:
        row.reverse()
    
    # Save result.
    try:
        save(image, new_image_path)
    except PermissionError:
        print("Permission denied.")
    except:
        print("New path error.")

# This function mirrors the image vertically.
def mirror_vertically(old_image_path, new_image_path):
    # Opens the image and get it as a matrix.
    try:
        image = load(old_image_path)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Initial path error.")

    # Mirror it vertically.
    image.reverse()

    # Save result.
    try:
        save(image, new_image_path)
    except PermissionError:
        print("Permission denied.")
    except:
        print("New path error.")