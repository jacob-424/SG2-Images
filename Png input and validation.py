"""
SG2: Processing of Images
CS 4500

This program processes grayscale png ballot images to find and verify specific alignment markers.
"""
from pathlib import Path

def Validation():

    while True:

        filename = input("Enter PNG File: ")

        if not filename.lower().endswith(".png"):
            print("Error: This is not a PNG file. Please try again. ")
            continue

        file_path = Path(filename)

        if not file_path.is_file():
            print(f"Error: '{filename}' doesn't exist in current directory.")
            continue

        if file_path.stat().st_size == 0:
            print(f"Error: '{filename}' is an empty file.")
            continue

        try:
            with open(file_path, 'rb') as f:
                header = f.read(8)
                if header != b'\x89PNG\r\n\x1a\n':
                    print(f"Error: '{filename}' is not a valid PNG file.")
                    continue
        except IOError:
            print(f"Error: Unable to open or read file '{filename}'.")
            continue

        print(f"\nSuccess: '{filename}' successfully loaded and verified")
        return file_path



def main():
    validated_file = Validation()
    print(f"Proceeding with file: {validated_file}")

if __name__ == "__main__":
    main()

