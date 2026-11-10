import numpy as np
import sys
from PIL import Image
from pathlib import Path

""" Programming language & IDE: Python with Thonny

    Team members: Andrew Hildebrand, Edwin Kihiuria, Jacob Wiley, Jeff Kimani, and Jesus Rivera Flores

    Date started: 10/22/26

    Major revision dates: 10/22/26

    Class: Introduction to the Software Profession

    Class number: CS 4500-001

    Program description:

    External files used:
"""

### Function documentation format.
""" Description of what the function does

    Args:
        arg_name (data type): Description of arg_name

    Returns:
        return_name (data type): Description of what the function returns

    Globals:
        global_name (data type): Description of the global variable used

    Sources:
        Add links to any sources used
"""

def programExplanation():
    """Explanation of SG2 program."""

    print("""
    ========================================
           SG2: PROCESSING OF IMAGES
    ========================================

    This program processes PNG images to detect 
    and verify alignment patterns.

    Steps performed:

    1. Validates the input PNG file.
    2. Converts the image into a pixel array.
    3. Searches for two 13x13 plus sign 
       pattern in a box.
    4. Checks the horizontal alignment
       of the detected patterns.
    5. Translates and displays the image.
    6. Reports image statistics.

    The image must contain exactly two
    matching patterns.

    ========================================
    """)

def convertImageToArr(filename):
    """ Converts a PNG image into a Numpy array with pixel values ranging from 0 to 255 in a grayscale.

        Args:
            filename (String): contains the name of the file to be converted

        Returns:
            image_to_arr (np.ndarray): holds the image as a np array.

        Sources:
            imageToArray function from SG1- Small Group 3.

    """
    # converts image to grayscale
    image_to_arr = Image.open(filename).convert("L")

    image_to_arr = np.array(image_to_arr, dtype=int)

    return image_to_arr


def patternDetection(image_arr):
    """ loops trough an image array and compares the pixels to match a specific pattern.
        The image is allowed to have only 2 patterns. if other number of patterns found,
        it prints a descriptive message and raises an error.

        Args:
            image_arr (np.ndarray): contains the image as a np array.

        Returns:
            coordinates (list[tuple[int,int]]): holds the coordinates found in the image as (row, column)

        Sources:
            patternLookup function from SG1- Small Group 3.

    """

    def patternMatch(window: np.ndarray, pattern: np.ndarray) -> bool:
        """ compares 2 numpy arrays to check if they have the same shape and values.

        Args:
            window (np.ndarray): contains a submatrix from the original image array.

            pattern (np.ndarray): contains the pattern to look for.

        Returns:
            "True" if the arrays match, "False otherwise"

        Sources:
            patternMatch function from SG1- Small Group 3.

        """

        # compare the elements only if the shapes are equal,
        # otherwise, print an error message and exit the program.
        if window.shape == pattern.shape:
            return np.array_equal(window, pattern)

        print("Error: pattern and window do not have the same shape")
        exit(1)

    pattern = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    # pattern = np.array([
    #    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    #    [0,0,0,0,0,0,0,0,0,0,0,0,0]])

    occurrences = 0
    coordinates = []
    row = 0
    column = 0

    image_rows = image_arr.shape[0]
    image_cols = image_arr.shape[1]

    pattern_rows = pattern.shape[0]
    pattern_cols = pattern.shape[1]

    # iterate over the entire target matrix, sliding a 11x11 submatrix over it.
    for row in range(image_rows - pattern_rows + 1):
        for column in range(image_cols - pattern_cols + 1):
            submatrix = image_arr[row:row + pattern_rows, column:column + pattern_cols]

            # check if the submatrix matches the pattern
            if patternMatch(submatrix, pattern):
                # add the central point coordinates to the list of coordinates
                location = (row + int(pattern_rows / 2), column + int(pattern_cols / 2))
                coordinates.append(location)
                occurrences += 1

    if occurrences != 2:
        print("Error: Exactly 2 pattern occurrences are allowed in the image.")
        if occurrences == 0:
            print("The image did not detect any pattern")
        else:
            print(f"Pattern occurrences: {len(coordinates)}")
            print(f"location: {coordinates}")
        #sys.exit(1)
        return None
    print(f"{len(coordinates)} Patterns found at the following locations: {coordinates}")

    return coordinates



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

    if coordinates[0][0] == coordinates[1][0]:
        print("These patterns share the same row coordinates.")
        print("These patterns are horizontally aligned!")
        return True
    else:
        print("ERROR: These patterns do not share the same row coordinates and are not horizontally aligned!")
        return False


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
    print("Image Statistics:")

    print(f"Height: {height} pixels")
    print(f"Width: {width} pixels")

    if min_grayness == max_grayness:
        print(f"Grayscale Range: {min_pixel}-{max_pixel} ({min_grayness})")
    else:
        print(f"Grayscale Range: {min_pixel}-{max_pixel} ({min_grayness} to {max_grayness})")

    print(f"Number of black pixels: {num_of_black}")
    print(f"Number of white pixels: {num_of_white}")

    print(f"Average pixel value: {avg_pixel:.2f} ({avg_grayness})")


def ImageTranslation(filename, coordinates):
    if len(coordinates) != 2:
        # Makes sure there's only two coordinates
        print("Error: Expected exactly two coordinates for the target pattern.")
        exit(1)

    # Determine which coordinate is the left one based on the column value
    if coordinates[0][1] < coordinates[1][1]:
        left_row_center, left_col_center = coordinates[0]
    else:
        left_row_center, left_col_center = coordinates[1]

    # Calculate the Shift Distance (X and Y)
    # shift_x, shift_y = calculateShiftDistance(target_pattern)
    pattern_top_left_row = left_row_center - 6
    pattern_top_left_col = left_col_center - 6

    Y = pattern_top_left_row
    X = pattern_top_left_col

    print(f"\nShifting image up by Y = {Y} pixels, and left by X = {X} pixels.")

    orig_img = Image.open(filename).convert("L")
    width, height = orig_img.size

    ballotY_img = Image.new("L", (width, height), color=0)

    # Shift the pixels from the old image to the new image
    for y_orig in range(height):
        for x_orig in range(width):
            # Calculate the new target destination coordinates
            new_y = y_orig - Y
            new_x = x_orig - X

            # Boundary check: only copy if the shifted pixel stays inside the canvas boundaries
            if 0 <= new_y < height and 0 <= new_x < width:
                pixel_value = orig_img.getpixel((x_orig, y_orig))
                ballotY_img.putpixel((new_x, new_y), pixel_value)

    # Save the translated image to disk
    ballotY_img.save("BallotY.png")
    print("Saved translated image as 'BallotY.png'")

    # Display both images to the user
    print("Displaying BallotX.png and BallotY.png...")
    orig_img.show()
    ballotY_img.show()

    # Pause and wait for the user to press ENTER before continuing to Task 5
    input("Press ENTER to continue")


def main():
    ...

    # TODO: 0) Print program explanation
    programExplanation()

    while True:
        # TODO: 1) PNG File input and validation
        validated_file = Validation()
        print(f"Proceeding with file: {validated_file}")

        # TODO: 2) Plus pattern detection
        arr_image = convertImageToArr(validated_file)
        coords_found = patternDetection(arr_image)

        if coords_found is None:
            continue

        # TODO: 3) Check pattern alignment
        aligned = check_pattern_alignment(coords_found)

        if not aligned:
            input("Press ENTER to try another PNG file")
            continue

        # TODO: 4) Move image and display
        ImageTranslation(validated_file, coords_found)

        # TODO: 5) Image statistics
        imageStats(arr_image)

        break


if __name__ == "__main__":
    main()
