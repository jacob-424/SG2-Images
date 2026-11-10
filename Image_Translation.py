from PIL import Image
import Png_input_and_validation

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

def main():
    coordinates = [(30, 40), (35, 100)] #Change to function name from Task 2 
    validated_file = Png_input_and_validation.Validation()
    ImageTranslation(validated_file, coordinates)

if __name__ == "__main__":
    main()