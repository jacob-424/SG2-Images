def display_introduction():
    
    print("                 BALLOT IMAGE PROCESSOR (SG2)\nThis program processes grayscale ballot images (.PNG) by:\n1. Validating your input .PNG filename, file existence, and format.\n2. Scanning the image to locate exactly two plus-sign patterns.\n3. Verifying that the two plus patterns are aligned horizontally.\n4. Shifting the image so the leftmost pattern aligns with (0,0), saving the translated result as 'BallotY.png'.\n5. Displaying both images and generating detailed image statistics.")

if __name__ == "__main__":
    display_introduction()