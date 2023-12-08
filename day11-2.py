# Re-importing necessary libraries and redefining the functions since the code execution state was reset
import numpy as np

# Original map
original_map = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]

original_map = open("input11.txt", "r").read().split()

# Function to identify empty rows and columns
def identify_empty_rows_cols(map_data):
    empty_rows = [i for i in range(len(map_data)) if "#" not in map_data[i]]
    empty_cols = [j for j in range(len(map_data[0])) if all(row[j] == '.' for row in map_data)]
    return empty_rows, empty_cols

# Function to mark galaxies with numbers
def mark_galaxies(map_data):
    galaxy_positions = {}
    galaxy_number = 1
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxy_positions[galaxy_number] = (i, j)
                galaxy_number += 1
    return galaxy_positions

# Function to calculate the sum of shortest paths with large scale expansion
def calculate_large_scale_distance(galaxy_positions, empty_rows, empty_cols, scale_factor):
    total_distance = 0
    for a in galaxy_positions:
        for b in galaxy_positions:
            if a != b:
                x1, y1 = galaxy_positions[a]
                x2, y2 = galaxy_positions[b]
                # Manhattan distance adjusted for expansion
                row_distance = abs(x1 - x2) + sum(1 for row in empty_rows if min(x1, x2) < row < max(x1, x2)) * (scale_factor - 1)
                col_distance = abs(y1 - y2) + sum(1 for col in empty_cols if min(y1, y2) < col < max(y1, y2)) * (scale_factor - 1)
                total_distance += row_distance + col_distance

    # Since we count each pair twice, divide by 2
    return total_distance / 2

# Identifying empty rows and columns
empty_rows, empty_cols = identify_empty_rows_cols(original_map)

# Marking galaxies with numbers
galaxy_positions = mark_galaxies(original_map)

# Scale factor for expansion
scale_factor = 1000000

# Calculate the total distance with the large scale expansion
total_large_scale_distance = calculate_large_scale_distance(galaxy_positions, empty_rows, empty_cols, scale_factor)
print("Part 2:", total_large_scale_distance)
