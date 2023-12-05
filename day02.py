# Python code to solve the Cube Conundrum

game_lines = open('input02.txt', 'r').readlines()

# The format of the input data has changed, so let's adjust the code to process each line.

# The bag's configuration
bag_config = {'red': 12, 'green': 13, 'blue': 14}



def is_game_possible(game_data, bag_config):
    # Each subset is separated by a semicolon
    subsets = game_data.split(';')

    for subset in subsets:
        # Each color and count within a subset is separated by a comma
        color_counts = subset.split(',')

        # Track the counts of cubes shown in this subset
        subset_config = {'red': 0, 'green': 0, 'blue': 0}

        # Parse the counts and colors
        for color_count in color_counts:
            count, color = color_count.strip().split(' ')
            count = int(count)
            color = color.strip()

            # If any count of a color exceeds what's available in the bag, the game is impossible
            if count > bag_config[color]:
                return False
            subset_config[color] += count

            # Also check if the total shown at any time exceeds the bag's capacity for a color
            if subset_config[color] > bag_config[color]:
                return False

    # If none of the subsets exceed the bag's capacity, the game is possible
    return True


# Function to parse a single line of game data
def parse_game_line(line):
    # Split the line into game ID and the color counts
    game_id_str, color_counts_str = line.split(':')
    game_id = int(game_id_str.split()[1])  # Extract the numeric ID

    return game_id, color_counts_str.strip()


# Function to determine the sum of the game IDs where the game is possible
def calculate_possible_games_sum(game_lines, bag_config):
    possible_games_sum = 0
    for line in game_lines:
        game_id, game_data = parse_game_line(line)
        if is_game_possible(game_data, bag_config):
            possible_games_sum += game_id
    return possible_games_sum

# Calculate the sum of the IDs of possible games based on the new format
print("Part 1:", calculate_possible_games_sum(game_lines, bag_config))


def find_minimum_cubes(game_data):
    # Each subset is separated by a semicolon
    subsets = game_data.split(';')

    # Initialize the minimum counts to 0
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}

    # Process each subset and update the minimum counts if necessary
    for subset in subsets:
        # Each color and count within a subset is separated by a comma
        color_counts = subset.split(',')

        # Temporary dictionary to hold counts for the current subset
        subset_counts = {'red': 0, 'green': 0, 'blue': 0}

        # Parse the counts and colors
        for color_count in color_counts:
            count, color = color_count.strip().split(' ')
            count = int(count)
            color = color.strip()

            # Update the subset counts
            subset_counts[color] += count

        # Update the minimum counts if the subset counts are higher
        for color in min_cubes:
            if subset_counts[color] > min_cubes[color]:
                min_cubes[color] = subset_counts[color]

    # Calculate the power of the set of cubes
    power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    return min_cubes, power


# Calculate the sum of the power of the minimum sets for all games
total_power_sum = 0
min_cubes_per_game = {}

for line in game_lines:
    game_id, game_data = parse_game_line(line)
    min_cubes, power = find_minimum_cubes(game_data)
    min_cubes_per_game[game_id] = min_cubes
    total_power_sum += power

print("Part 2:", total_power_sum)
