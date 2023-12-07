# The puzzle involves calculating the number of ways to beat the record for each race and multiplying these numbers together.

def calculate_ways_to_win(time, distance):
    """Calculate the number of ways to win the race."""
    ways_to_win = 0
    for button_hold_time in range(time):
        travel_time = time - button_hold_time
        travel_distance = button_hold_time * travel_time
        if travel_distance > distance:
            ways_to_win += 1
    return ways_to_win

# Given race times and distances
race_times = [7, 15, 30]
race_distances = [9, 40, 200]

race_times = [44899691]
race_distances = [277113618901768]

# Calculating the number of ways to win for each race
ways_to_win_each_race = [calculate_ways_to_win(time, distance) for time, distance in zip(race_times, race_distances)]

# Multiplying these numbers together
total_ways_to_win = 1
for ways in ways_to_win_each_race:
    total_ways_to_win *= ways

print("Part 1:", total_ways_to_win, ways_to_win_each_race)

