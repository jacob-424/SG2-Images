import numpy as np
import sys
from PIL import Image

pattern = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0]])

def convertImageToArr(filename):
    # converts image to grayscale
    image = Image.open(filename).convert("L")

    zerosAndOnes = []

    # sets number of rows to image height
    for y in range(image.height):
        row = []

        # sets number of columns to image width
        for x in range(image.width):
            pixel = image.getpixel((x, y))

            # black pixel -> 0
            if pixel == 0:
                row.append(0)
            # white pixel -> 1
            else:
                row.append(1)

        zerosAndOnes.append(row)

    return np.array(zerosAndOnes, dtype=int)

def patternDetection(image):
    
    def patternMatch(window: np.ndarray, pattern: np.ndarray) -> bool:
        
        #compare the elements only if the shapes are equal,
        #otherwise, print an error message and exit the program.
        if window.shape == pattern.shape:
            return np.array_equal(window, pattern)
        
        print("Error: pattern and window do not have the same shape")
        exit(1)
        
    occurrences = 0
    coordinates = []
    row = 0
    column = 0
    
    arr_image = convertImageToArr(image)
    image_rows = arr_image.shape[0]
    image_cols = arr_image.shape[1]
    
    pattern_rows = pattern.shape[0]
    pattern_cols = pattern.shape[1]
    
    #iterate over the entire target matrix, sliding a 11x11 submatrix over it.
    for row in range (image_rows - pattern_rows - 1):
        for column in range(image_cols - pattern_cols - 1):
            submatrix = arr_image[row:row + pattern_rows, column:column + pattern_cols]
            
            # check if the submatrix matches the pattern
            if patternMatch(submatrix, pattern):
                #add the central point coordinates to the list of coordinates
                location = (row + int(pattern_rows/2), column + int(pattern_cols/2))
                coordinates.append(location)
                occurrences += 1
                
    if occurrences != 2:
        print("Error: Exactly 2 pattern occurrences are allowed in the image.")
        if occurrences == 0:
            print("The image did not detect any pattern")
        else:
            print(f"Pattern occurrences: {len(coordinates)}")
            print(f"location: {coordinates}")
        exit(1)
    print(f"{len(coordinates)} Patterns found at the following locations: {coordinates}")
            
    return coordinates

patternDetection('BallotX.png')