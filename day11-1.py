import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

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


# Function to expand the universe
def expand_universe(map_data):
    # Identify empty rows and columns
    empty_rows = [i for i in range(len(map_data)) if "#" not in map_data[i]]
    empty_cols = [j for j in range(len(map_data[0])) if all(row[j] == '.' for row in map_data)]

    # Duplicate empty rows and columns
    expanded_map = []
    for i, row in enumerate(map_data):
        new_row = "".join(cell * 2 if j in empty_cols else cell for j, cell in enumerate(row))
        expanded_map.append(new_row)
        if i in empty_rows:
            expanded_map.append(new_row)

    return expanded_map


# Function to create a graph from the expanded map
def create_graph(expanded_map):
    # Marking galaxies with numbers
    galaxy_positions = {}
    galaxy_number = 1
    for i, row in enumerate(expanded_map):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxy_positions[galaxy_number] = (i, j)
                galaxy_number += 1

    # Creating a graph
    size = len(galaxy_positions)
    graph = np.zeros((size, size))

    for a in galaxy_positions:
        for b in galaxy_positions:
            if a != b:
                x1, y1 = galaxy_positions[a]
                x2, y2 = galaxy_positions[b]
                # Manhattan distance
                graph[a - 1][b - 1] = abs(x1 - x2) + abs(y1 - y2)

    return graph


# Function to calculate the sum of shortest paths
def sum_of_shortest_paths(graph):
    # Compute the shortest paths using Floyd-Warshall algorithm
    distances = shortest_path(csr_matrix(graph), method='FW')
    # Summing up the shortest distances
    return np.sum(np.triu(distances))


# Expanding the universe
expanded_map = expand_universe(original_map)

# Creating a graph
graph = create_graph(expanded_map)

# Calculating the sum of shortest paths
total_distance = sum_of_shortest_paths(graph)
print("Part 1:", total_distance)
