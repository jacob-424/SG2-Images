import random

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

### Parameters

rows = 50
bits_per_row = 50

# How many patterns should be inserted.
insert_first_pattern = True
insert_second_pattern = True

# Starting positions for the first and second pattern.
# Positions are zero-based. i.e. if there are 40 rows, then row 39 is the final one, etc.
# Positions start from the top left of the pattern.
# Note that if you choose a location too close to the bottom or right edges of the file, the pattern will be cut off.
start1_row = 5
start1_col = 8

start2_row = 28
start2_col = 25

# Generate random binary data
data = []

for _ in range(rows):
    row = random.choices("01", k=bits_per_row)
    data.append(row)

# Add first pattern
if insert_first_pattern:
    # Insert the pattern, cutting it off at the edges if necessary
    for r in range(min(len(pattern), rows - start1_row)):
        for c in range(min(len(pattern[r]), bits_per_row - start1_col)):
            data[start1_row + r][start1_col + c] = pattern[r][c]

# Add second pattern
if insert_second_pattern:
    # Insert the pattern, cutting it off at the edges if necessary
    for r in range(min(len(pattern), rows - start2_row)):
        for c in range(min(len(pattern[r]), bits_per_row - start2_col)):
            data[start2_row + r][start2_col + c] = pattern[r][c]

# Write the file
with open("binary.txt", "w", encoding="utf-8") as file:
    for row in data:
        file.write("".join(row) + "\n")