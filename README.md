# Imager

**Imager is a program to edit PNG images.**

It has been designed to mirror images, rotate them, or convert them to greyscale.
This project has been made with the intention to get acquainted with matrices and pixels.

## Index
 - [Usage](#usage)
 - [Commands]()

----

# Usage

To use this program follow these steps:

1. Download all the files from GitHub.
2. Open the terminal.
3. Move to the directory where the project is located.
4. Make sure to have python installed on your computer.
5. Run the main file ***imager.py*** using the following command:
   
   `python imager.py`

## Commands

This program supports 2 types of commands: editing commands and general commands.
 - General commands
   - `/help`
     <br> Print the list of commands, general instructions and the name of the project.
   - `/information`
     <br> Print the author and the license of the program.
   - `/exit`
     <br> Exit the program.

 - Editing commands
   - `-mr`
     <br> Mirror the image. There are two options: `-h` and `-v`, the former mirrors the image horizontally,
     the latter mirrors it vertically. If no option is specified, the image is mirrored horizontally.
   - `-bw`
     <br> Make the image black and white.
   - `rt`
     <br> Rotate the image. There are two options: `-90` and `-270`, the former rotates it by 90 degrees,
     the latter rotates it by 270 degrees. If no option is specified, the image is rotated by 90 degrees.
     There is no option for 180 degrees because it can be obtained just by mirroring the image vertically.
