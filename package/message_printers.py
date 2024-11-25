# This file contains all the functions used by the main program to
# display messages, instructions and information.

# This function prints the header of the program with all
# available commands.
def print_header() -> None:
    print()

    print("+---------------------------- IMAGER ----------------------------+")
    print("|                                                                |")
    print("|  Use this program to edit PNG images.                          |")
    print("|                                                                |")
    print("|  General commands start with '/'.                              |")
    print("|  Editing commands have the prefix '-'.                         |")
    print("|    To execute an editing command use the following format:     |")
    print("|    <command> <option> <image path> <result image path>         |")
    print("|    i.e. :   -mr -v image.png mirrored_image.png                |")
    print("|                                                                |")
    print("|  Commands:                                                     |")
    print("|  Editing commands:                                             |")
    print("|     -mr                   - Mirror the image                   |")
    print("|        -h                    - Horizontally (default)          |")
    print("|        -v                    - Vertically                      |")
    print("|     -bw                   - Make the image black and white     |")
    print("|     -rt                   - Rotate the image                   |")
    print("|        -90                   - by 90 degrees (-270)            |")
    print("|        -270                  - by 270 degrees (-90)            |")
    print("|   General commands:                                            |")
    print("|     /help                 - Print this message again           |")
    print("|     /information          - Print useful information           |")
    print("|     /exit                 - Close this program                 |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")

# This function prints information about the project.
def print_information() -> None:
    print()

    print("+----------------------- INFORMATION ------------------------+")
    print("|                                                            |")
    print("|  Author:                                                   |")
    print("|    Nicolo Alesi                                            |")
    print("|                                                            |")
    print("|  License: MIT License                                      |")
    print("|                                                            |")
    print("+------------------------------------------------------------+")