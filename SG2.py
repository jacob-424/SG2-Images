import numpy as np
import sys
from PIL import Image

""" Programming language & IDE: Python with Thonny

    Team members: Andrew Hildebrand, Edwin Kihiuria, Jacob Wiley, Jeff Kimani, and Jesus Rivera Flores
    
    Date started: 10/22/26
    
    Major revision dates: 10/22/26
                          
    Class: Introduction to the Software Profession
    
    Class number: CS 4500-001
    
    Program description:
    
    Central Data Structures:
    
    External files used:
    
    Sources:
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
    
    #iterate over the entire target matrix, sliding a 11x11 submatrix over it.
    for row in range (image_rows - pattern_rows - 1):
        for column in range(image_cols - pattern_cols - 1):
            submatrix = image_arr[row:row + pattern_rows, column:column + pattern_cols]
            
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
        sys.exit(1)
    print(f"{len(coordinates)} Patterns found at the following locations: {coordinates}")
            
    return coordinates

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
    print("BallotX.png Statistics:")
    
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
    ...
    
    # TODO: 0) Print program explanation
    
    # TODO: 1) PNG File input and validation
    
    # TODO: 2) Plus pattern detection
    arr_image = convertImageToArr('BallotX.png')
    coords_found = patternDetection(arr_image)
    
    # TODO: 3) Check pattern alignment
    
    # TODO: 4) Move image and display
    
    # TODO: 5) Image statistics
    imageStats(arr_image)
    
    
if __name__ == "__main__":
    main()