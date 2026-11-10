"""
SG2: Processing of Images
CS 4500

This program processes grayscale png ballot images to find and verify specific alignment markers.

Sources: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions, https://www.w3schools.com/python/python_user_input.asp
"""
from pathlib import Path
from PIL import Image

def Validation():

    # Find the directory
    program_directory = Path(__file__).resolve().parent

    while True:

        filename = input("Enter PNG File: ").strip()

        if not filename.endswith(".PNG"):
            print("Error: This is not a PNG file. Please try again. ")
            continue

        # Makes sure the user enters only a filename and not a path
        if "/" in filename or "\\" in filename or ":" in filename:
            print("Error: File must be in the same directory as the program.")
            continue

        # Create the complete file path
        file_path = (program_directory / filename).resolve()

         # Make sure the file is actually inside the program directory.
        if file_path.parent != program_directory:
            print("Error: File must be in the same directory as the program.")
            continue

        # Check whether the file exists.
        if not file_path.is_file():
            print(f"Error: '{filename}' doesn't exist in current directory.")
            continue

        # Check whether the file is empty.
        try:
            if file_path.stat().st_size == 0:
                print(f"Error: '{filename}' is an empty file.")
                continue

        except OSError:
            print(f"Error: Unable to access file '{filename}'.")
            continue

        # Verify that the file is an actual, readable PNG image.
        try:

            # Open the image and check its format.
            with Image.open(file_path) as image:

                if image.format != "PNG":
                    print(f"Error: '{filename}' is not a valid PNG image.")
                    continue

                # Verify the image structure.
                image.verify()

            # Reopen the image and load its pixel data.
            with Image.open(file_path) as image:
                image.load()

        except (OSError, SyntaxError, ValueError, Image.DecompressionBombError):
            print(f"Error: '{filename}' is corrupted or is not a valid PNG image.")
            continue

        print(f"\nSuccess: '{filename}' successfully loaded and verified")
        return file_path



def main():
    validated_file = Validation()
    print(f"Proceeding with file: {validated_file}")

if __name__ == "__main__":
    main()

