import random
import tkinter as tk

def dataGen(rows, cols, *starts):
    """
        Args:
            rows: total number of rows
            cols: total number of columns
            starts: list of tuples that contain the (row, col) location of each plus pattern.
    """
    
    # Pattern is 13x13 digits
    pattern = [
        "0000000000000",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0000000000000",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0111110111110",
        "0000000000000"
    ]

    # Generate random binary data
    data = []
    for _ in range(rows):
        row = random.choices("01", k=cols)
        data.append(row)

    # Insert a pattern at each given location
    for start_row, start_col in starts:
        # Cut the pattern off at the edges if necessary
        for r in range(min(len(pattern), rows - start_row)):
            for c in range(min(len(pattern[r]), cols - start_col)):
                data[start_row + r][start_col + c] = pattern[r][c]

    return data

def outputBallotX(data):
    num_of_rows = len(data)
    num_of_cols = len(data[0])

    img = tk.PhotoImage(width=num_of_cols, height=num_of_rows)

    # Create pixels
    for y, row in enumerate(data):
        for x, bit in enumerate(row):
            if bit in (0, '0'):
                img.put(data="black", to=(x, y))
            elif bit in (1, '1'):
                img.put(data="white", to=(x, y))

    # Attempt to save img as IMAGE1.png
    try:
        img.write(filename="BallotX.png")
    except tk.TclError as e:
        print(f"Failed to save image: {e}")
        return False

    return True
        
def main():
    
    root = tk.Tk() # Initialize tkinter
    root.withdraw() # Hide main window
    
    # Edit parameters as needed.
    # First two are the total number of rows and columns, after that is any number of tuples for each plus pattern location.
    # Note that a pattern location is (row, col), where row and col start counting from zero.
    # Each tuple is the location of the top left most bit of the plus pattern.
    data = dataGen(50, 50, (8, 5), (35, 35))
    
    outputBallotX(data)
    
if __name__ == "__main__":
    main()