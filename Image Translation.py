from PIL import Image

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

    #Calculate the Shift Distance (X and Y)
    #shift_x, shift_y = calculateShiftDistance(target_pattern)
    pattern_top_left_row = left_row_center - 6
    pattern_top_left_col = left_col_center - 6

    Y = pattern_top_left_row
    X = pattern_top_left_col

    print(f"\nShifting image up by Y = {Y} pixels, and left by X = {X} pixels.")

    orig_img = Image.open(filename)
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
    coordinates = "Step 2 Coordinates"
    validated_file = "Step 1 Validation"
    ImageTranslation(validated_file, coordinates)