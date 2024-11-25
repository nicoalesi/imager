# This file contains all the functions used by the main program
# to edit images.

from package.utils import *

# This is a list containing all the exportable functions of this file.
__all__ = [
    "make_bw",
    "mirror_horizontally",
    "mirror_vertically",
    "rotate_90",
    "rotate_270",
]

# This function mirrors an image horizontally.
def mirror_horizontally(old_image_path: str, new_image_path: str) -> None:
    # Opens the image and get it as a matrix.
    try:
        image: list(list((int, int, int))) = load(old_image_path)
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
def mirror_vertically(old_image_path: str, new_image_path: str) -> None:
    # Opens the image and get it as a matrix.
    try:
        image: list(list((int, int, int))) = load(old_image_path)
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


# This function makes the image black and white.
def make_bw(old_image_path: str, new_image_path: str) -> None:
    # Opens the image and get it as a matrix.
    try:
        image: list(list((int, int, int))) = load(old_image_path)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Initial path error.")

    # Make it black and white.
    for row in image:
        for i in range(len(row)):
            row[i] = make_pix_grey(row[i])

    # Save result.
    try:
        save(image, new_image_path)
    except PermissionError:
        print("Permission denied.")
    except:
        print("New path error.")


# This function rotates the image by 90 degrees.
def rotate_90(old_image_path: str, new_image_path: str) -> None:
    # Opens the image and get it as a matrix.
    try:
        image: list(list((int, int, int))) = load(old_image_path)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Initial path error.")

    # Rotate the image by 90 degrees.
    #   To perform a 90 degrees rotation is sufficient to take the
    #   transposed of the initial matrix and mirror it horizontally.

    # Create the transposed matrix.
    transposed: list(list((int, int, int))) = list(zip(*copy_matrix(image)))
    # Remove all elements from image's initial matrix.
    image.clear()
    # Append every row of the transposed matrix to image and reverse it.
    for index, row in enumerate(transposed):
        image.append(list(row))
        image[index].reverse()
    
    # Save result.
    try:
        save(image, new_image_path)
    except PermissionError:
        print("Permission denied.")
    except:
        print("New path error.")
    

# This function rotates an image by 270 degrees.
def rotate_270(old_image_path: str, new_image_path: str) -> None:
    # Opens the image and get it as a matrix.
    try:
        image: list(list((int, int, int))) = load(old_image_path)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Initial path error.")
    
    # Rotate the image by 270 degrees.
    #   To perform a 270 degrees rotation is sufficient to take the
    #   transposed of the initial matrix and mirror it vertically.

    # Create the transposed matrix.
    transposed: list(list((int, int, int))) = list(zip(*copy_matrix(image)))
    # Remove all elements from image's initial matrix.
    image.clear()
    # Append every row of the transposed matrix to image.
    for row in transposed:
        image.append(list(row))
    # Reverse the whole matrix to obtain the vertically mirrored version.
    image.reverse()

    # Save result.
    try:
        save(image, new_image_path)
    except PermissionError:
        print("Permission denied.")
    except:
        print("New path error.")
