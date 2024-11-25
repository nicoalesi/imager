# This file contains all the useful and secondary functions used
# by the program and its editors.
#
# The functions "load" and "save" have been written by my university lecturers.

from package.png import from_array, Reader

# This is a list containing all the exportable functions of this file.
__all__ = [
    "copy_matrix",
    "load",
    "make_pix_grey",
    "save",
]

# This function opens a PNG image and returns a matrix (list of lists)
# with all the pixels of the image represented as triples (R, G, B);
# Every color has a value between 0 and 255.
def load(filename: str) -> list(list((int, int, int))):
    with open(filename, mode='rb') as f:
        reader = Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        w *= 3
        return [ [ (line[i],line[i+1],line[i+2]) 
                   for i in range(0, w, 3) ]
                 for line in png_img ]


# This functions saves the image as a PNG file
def save(img: list(list((int, int, int))), filename: str) -> None:
    pngimg = from_array(img,'RGB')
    pngimg.save(filename)


# This function gets a pixel as (R, G, B) as input and returns
# its greyscale version.
def make_pix_grey(pixel: (int, int, int)) -> (int, int, int):
    # Calculate the average of RGB values.
    average: int = sum(pixel) // 3
    # Return a pixel with RGB values all equal to average.
    return (average,) * 3


# This function creates a deep copy of a matrix.
def copy_matrix(matrix: list) -> list:
    return [ l.copy() for l in matrix ]
