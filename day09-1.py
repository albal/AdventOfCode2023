def extrapolate_next_value(history):
    """
    Extrapolates the next value in the history by generating sequences of differences
    and using them to predict the next number.
    """
    # Generate the initial sequence of differences
    sequences = [history]
    while True:
        current_sequence = sequences[-1]
        next_sequence = [current_sequence[i+1] - current_sequence[i] for i in range(len(current_sequence)-1)]
        sequences.append(next_sequence)
        # If the next sequence is all zeroes, break the loop
        if all(v == 0 for v in next_sequence):
            break

    # Work out the next value from the bottom up
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    # The next value is the last element of the original sequence
    return sequences[0][-1]

# Example data
data = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

data = []

data12 = open("input09.txt", "r").readlines()

for line in data12:
    new_line = list(map(int ,line.strip().split(' ')))
    print(new_line)
    data.append(new_line)

# Sum of extrapolated values for each history
print("Part 1:", sum(extrapolate_next_value(history) for history in data))
