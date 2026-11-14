import tkinter as tk
import numpy as np
import sys
from PIL import Image
from pathlib import Path

""" Programming language & IDE: Python with Thonny

    Team members: Andrew Hildebrand, Edwin Kihiuria, Jacob Wiley, Jeff Kimani, and Jesus Rivera Flores
    
    Date started: 10/22/26
    
    Major revision dates:
    
        * 10/22/26: Project Started
        * 11/11/2026: Merged All functions into the main file
        
                          
    Class: Introduction to the Software Profession
    
    Class number: CS 4500-001
    
    Program description:
    SG2: Ballot Image Processor.
    This program processes and analyzes grayscale ballot images (.PNG).
    The program performs the following operations:
    1. Input Validation: Prompts the user to enter a PNG filename and verifies that
        the file exists and is in .PNG format.
    2. Pattern Detection: The Program scans the grayscale ballot image to locate exactly 2 patterns
    3. Allignment Verification: The program checks that both patterns detected are
        horizontailly alligned.
    4. Image Translation: The image is shifted so that the leftmost pattern is alligned
        with the (0,0) pixel.The translated Image is saved as BallotY.PNG and
        displayed to the screen.
    5. Image Statistics: Detailed statistics about the original image is displayed to the screen
    
    External files used:
        * https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions, https://www.w3schools.com/python/python_user_input.asp
        * Functions adapted from SG1 - Small Group 3
        * https://www.geeksforgeeks.org/numpy/numpy-array-functions/
"""

def display_introduction():
    """
    Prints a description of the program to the screen
    """
    
    print("                 BALLOT IMAGE PROCESSOR (SG2)\nThis program processes grayscale ballot images (.PNG) by:\n1. Validating your input .PNG filename, file existence, and format.\n2. Scanning the image to locate exactly two plus-sign patterns.\n3. Verifying that the two plus patterns are aligned horizontally.\n4. Shifting the image so the leftmost pattern aligns with (0,0), saving the translated result as 'BallotY.png'.\n5. Displaying both images and generating detailed image statistics.")


def Validation():
    """
    SG2: Processing of Images
    CS 4500

    This program processes grayscale png ballot images to find and verify specific alignment markers.

    Sources: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions, https://www.w3schools.com/python/python_user_input.asp
    """
    # Find the directory
    program_directory = Path(__file__).resolve().parent

    while True:

        filename = input("Enter PNG File: ").strip()

        if not filename.lower().endswith(".png"):
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
            
            
            
def convertImageToArr(filename: str) -> np.ndarray:
    """ Converts a PNG image into a Numpy array with pixel values ranging from 0 to 255 in a grayscale.
    
        Args:
            filename (str): contains the name of the file to be converted
        
        Returns:
            image_to_arr (np.ndarray): holds the image as a np array.
            
        Sources:
            Adapted from the imageToArray function from SG1- Small Group 3.
            the original code was modified to meet the requirements of this project.
    """
    # converts image to grayscale
    image_to_arr = Image.open(filename).convert("L")

        
    image_to_arr = np.array(image_to_arr, dtype=int)

    return image_to_arr

def patternDetection(image_arr: np.ndarray) -> list[tuple[int,int]]:
    """ loops trough an image array and compares the pixels to match a specific pattern.
        The image is allowed to have only 2 patterns. if other number of patterns found,
        it prints a descriptive message and raises an error.
        
        Args:
            image_arr (np.ndarray): contains the image as a np array.
        
        Returns:
            coordinates (list[tuple[int,int]]): holds the coordinates found in the image as (row, column)
            
        Sources:
            Adapted from the patternLookup function from SG1- Small Group 3.
            the original code was modified to meet the requirements of this project.           
    """
    
    def patternMatch(window: np.ndarray, pattern: np.ndarray) -> bool:
        """ compares 2 numpy arrays to check if they have the same shape and values.
        
        Args:
            window (np.ndarray): contains a submatrix from the original image array.
            
            pattern (np.ndarray): contains the pattern to look for. 
        
        Returns:
            "True" if the arrays match, "False otherwise"
            
        Sources:
            Adapted from the patternMatch function from SG1- Small Group 3.
            the original code was modified to meet the requirements of this project.
        """
        
        #compare the elements only if the shapes are equal,
        #otherwise, print an error message and exit the program.
        if window.shape == pattern.shape:
            return np.array_equal(window, pattern)
        
        print("Error: pattern and window do not have the same shape")
        exit(1)
   
   
    pattern = np.array([
        [0, 0,  0,  0,  0,  0, 0, 0,  0,  0,  0,  0, 0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0, 0,  0,  0,  0,  0, 0, 0,  0,  0,  0,  0, 0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0,255,255,255,255,255,0,255,255,255,255,255,0],
        [0, 0,  0,  0,  0,  0, 0, 0,  0,  0,  0,  0, 0]])

    occurrences = 0
    coordinates = []
    row = 0
    column = 0
    
    image_rows = image_arr.shape[0]
    image_cols = image_arr.shape[1]
    
    pattern_rows = pattern.shape[0]
    pattern_cols = pattern.shape[1]
    
    #iterate over the entire target matrix, sliding a 11x11 submatrix over it.
    for row in range (image_rows - pattern_rows + 1):
        for column in range(image_cols - pattern_cols + 1):
            submatrix = image_arr[row:row + pattern_rows, column:column + pattern_cols]
            
            # check if the submatrix matches the pattern
            if patternMatch(submatrix, pattern):
                #add the central point coordinates to the list of coordinates
                location = (row + int(pattern_rows/2), column + int(pattern_cols/2))
                coordinates.append(location)
                occurrences += 1
                
    # Raise error if the pattern does not appear 2 times 
    if occurrences != 2:
        print("Pattern Detection Error: Exactly 2 pattern occurrences are allowed in the image.")
        if occurrences == 0:
            print("The image did not detect any pattern")
        else:
            print(f"Pattern occurrences: {len(coordinates)}")
            print(f"location: {coordinates}")
        
        print("Try a different File!\n")
        return None

    # Print the coordinates
    print(f"{len(coordinates)} Patterns found at the following locations: {coordinates}")
    
    # Make sure the patterns do not overlap. 
    if abs(coordinates[0][0] - coordinates[1][0]) < pattern_rows and abs(coordinates[0][1] - coordinates[1][1]) < pattern_cols:
        print("Error. The patterns must not share any pixels.")
        print("Try a different File!\n")
        return None
    return coordinates

def check_pattern_alignment(coordinates):
    """ This function compares the coordinate values returned from the "patternDetection" function, checking
        for horizontal alignment between the detected patterns based on row values of pattern center.
        Globals:
            None
        Args:
            coordinates - represents a list containing two integer tuples representing the center coordinates
            of patterns 1 and 2. coordinates are represented as (row,column). 
        
        Returns:
            True if the center coordinates share the same row and are horizontally aligned
            False otherwise
            
        """
    
    print(f"\tPattern 1 has size of 13 x 13 with center located at {coordinates[0]}.")
    print(f"\tPattern 2 has size of 13 x 13 with center located at {coordinates[1]}.")
    
    if (coordinates[0][0] == coordinates[1][0]):
        print("These patterns share the same row coordinates.")
        print("These patterns are horizontally aligned!")
        return True
    else:
        print("ERROR: These patterns do not share the same row coordinates and are not horizontally aligned!")
        return False
        

def ImageTranslation(filename, coordinates):
    """
    Translates the image so the upper-left corner of the
    leftmost detected pattern is at (0, 0).
    
    Saves the translated image as BallotY.png and
    displays both images for comparison.
    """

    if len(coordinates) != 2:
        # Makes sure there's only two coordinates
        print("Error: Expected exactly two coordinates for the target pattern.")
        exit(1)

    # Determine which coordinate is the left one based on the column value
    if coordinates[0][1] < coordinates[1][1]:
        left_row_center, left_col_center = coordinates[0]
    else:
        left_row_center, left_col_center = coordinates[1]

    # Find the upper-left corner of the leftmost pattern.
    # The pattern is 13 x 13, so its center is 6 pixels
    # away from its upper-left corner.
    pattern_top_left_row = left_row_center - 6
    pattern_top_left_col = left_col_center - 6

    # Calculate the number of pixels to move.
    Y = pattern_top_left_row
    X = pattern_top_left_col

    print(f"\nShifting image up by Y = {Y} pixels, and left by X = {X} pixels.")

    # Open the original image and create a copy of its pixels.
    with Image.open(filename) as original_image:
        orig_img = original_image.convert("L")
        width, height = orig_img.size
    
        # Create a new black image with the same dimensions.
        ballotY_img = Image.new("L", (width, height), color=0)
    
     # Shift the pixels from the old image to the new image
        for y_orig in range(height):
            for x_orig in range(width):

                # Calculate the new coordinates
                new_y = y_orig - Y
                new_x = x_orig - X
            
                # Boundary check: only copy if the shifted pixel stays inside the canvas boundaries
                if 0 <= new_y < height and 0 <= new_x < width:

                    pixel_value = orig_img.getpixel((x_orig, y_orig))
                    ballotY_img.putpixel((new_x, new_y), pixel_value)

        # Keep a copy of the original image for display.
        original_display = orig_img.copy()

    # Save BallotY.png in the same directory as BallotX.png.
    output_path = filename.parent / "BallotY.png"
    ballotY_img.save(output_path, format="PNG")

    print(f"Saved translated image as '{output_path}'")
    
    # Display both images to the user
    print("Displaying BallotX.png and BallotY.png")

    original_display.show()
    ballotY_img.show()
    
    # Pause and wait for the user to press ENTER before continuing to Task 5
    input("Press ENTER to continue")

    # Close the images.
    original_display.close()
    orig_img.close()
    ballotY_img.close()
    
def getGrayness(pixel):
    """ Returns the grayscale color that pixel represents.

    Args:
        pixel (int or float): A value in the range of 0-255
        
    Returns:
        grayness (string): The color of pixel, either black, dark gray, gray, light gray, or white
    """
    grayness = ""
    
    if pixel <= 50:
        grayness = "Black"
    elif pixel <= 101:
        grayness = "Dark Gray"
    elif pixel <= 153:
        grayness = "Gray"
    elif pixel <= 204:
        grayness = "Light Gray"
    elif pixel <= 255:
        grayness = "White"
        
    return grayness

def imageStats(arr_image):
    """ Outputs various statistics about BallotX.png including height/width, range of pixel values,
        the number of black and white pixels, and the average pixel value.

    Args:
        arr_image (np.ndarray): BallotX.png as an array of pixel values between 0-255
    
    Sources:
        https://www.geeksforgeeks.org/numpy/numpy-array-functions/
    """
    ### Collect stats
    height = arr_image.shape[0]
    width = arr_image.shape[1]
    
    # Get range of pixel values and the grayscale color
    min_pixel = arr_image.min()
    min_grayness = getGrayness(min_pixel)
    max_pixel = arr_image.max()
    max_grayness = getGrayness(max_pixel)
    
    # Get the number of black and white pixels
    num_of_black = np.sum(arr_image == 0)
    num_of_white = np.sum(arr_image == 255)
    
    # Get the average value of each pixel
    avg_pixel = arr_image.mean()
    avg_grayness = getGrayness(avg_pixel)
    
    ### Output stats
    print("\nBallotX.png Statistics:")
    
    print(f"Height: {height} pixels")
    print(f"Width: {width} pixels")
    
    if min_grayness == max_grayness:
        print(f"Grayscale Range: {min_pixel}-{max_pixel} ({min_grayness})")
    else:
        print(f"Grayscale Range: {min_pixel}-{max_pixel} ({min_grayness} to {max_grayness})")
        
    print(f"Number of black pixels: {num_of_black}")
    print(f"Number of white pixels: {num_of_white}")
        
    print(f"Average pixel value: {avg_pixel:.2f} ({avg_grayness})")

            
def main():
    """
    Controls the main program flow by calling the
    validation, conversion, detection, alignment,
    translation, and statistics functions.
    
    Allows the user to retry if detection or
    alignment fails.
    """
    display_introduction()
    aligned = False
    while not aligned:
        while True:
            validated_file = Validation()
            print(f"Proceeding with file: {validated_file}\n")
            arr_image = convertImageToArr(validated_file)
            coords_found = patternDetection(arr_image)
            if coords_found is not None:
                break
        
        aligned = check_pattern_alignment(coords_found)
        if not aligned:
            input("Press ENTER to try a different file.")
    ImageTranslation(validated_file, coords_found)
    imageStats(arr_image)

if __name__ == "__main__":
    main()
