# This file contains the main program.

from package.message_printers import *

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

        # Perform matching operations.
        match elements[0][0]:
            case "-":
                # Calculate the number of elements.
                n_elements: int = len(elements)

                # If less than 3 
                if n_elements < 3:
                    print("Too few arguments.")
                    continue

                match elements[0]:
                    case "-mr":
                        match elements[1]:
                            case "-h":
                                ...
                            case "-v":
                                ...
                            case _:
                                ...
                    case "-bw":
                        ...
                    case "-rt":
                        match elements[1]:
                            case "-90":
                                ...
                            case "-270":
                                ...
                            case _:
                                ...
                    case _:
                        print("Command not found.")
            case "/":
                match command:
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