# This file contains the main program.

from package.message_printers import *
from package.editors import *

# MAIN function.
def main() -> None:
    # Print header.
    print_header()

    # Loop to catch commands.
    while True:
        # Get the command as input.
        command: str = input("Command: ")
        # Split the command to get its elements.
        elements: list(str) = command.split()
        # Store the main command in a variable.
        main_command: str = elements[0]

        # Perform matching operations.
        #   Check the first char to understand whether it's a general
        #   or editing command.
        match main_command[0]:
            case "-":
                # Calculate the number of elements.
                n_elements: int = len(elements)

                # If less than 3 arguments are inputted, print
                # an error and ask for a command again.
                if n_elements < 3:
                    print("Too few arguments.")
                    continue

                # Assign every element to a variable for readability.
                if n_elements == 3:
                    option: str = "default"
                    old_image_path: str = elements[1]
                    new_image_path: str = elements[2]
                else:
                    option: str = elements[1]
                    old_image_path: str = elements[2]
                    new_image_path: str = elements[3]

                match main_command:
                    case "-mr":
                        match option:
                            case "-h" | "default":
                                mirror_horizontally(old_image_path, \
                                                    new_image_path)
                            case "-v":
                                mirror_vertically(old_image_path, \
                                                  new_image_path)
                    case "-bw":
                        make_bw(old_image_path, new_image_path)
                    case "-rt":
                        match option:
                            case "-90" | "default":
                                rotate_90(old_image_path, new_image_path)
                            case "-270":
                                rotate_270(old_image_path, new_image_path)
                    case _:
                        print("Command not found.")
            case "/":
                match main_command:
                    case "/help":
                        print_header()
                    case "/information":
                        print_information()
                    case "/exit":
                        break
                    case _:
                        print("Command not found.")
            case _:
                print("Command not found.")


if __name__ == "__main__":
    main()
