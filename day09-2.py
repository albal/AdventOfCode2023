def extrapolate_previous_value(history):
    """
    Extrapolates the previous value in the history by generating sequences of differences
    and using them to predict the previous number, working backwards.
    """
    sequences = [history]
    while True:
        current_sequence = sequences[-1]
        next_sequence = [current_sequence[i+1] - current_sequence[i] for i in range(len(current_sequence)-1)]
        sequences.append(next_sequence)
        if all(v == 0 for v in next_sequence):
            break

    # Add a zero at the beginning of the sequence of zeroes
    sequences[-1].insert(0, 0)

    # Work out the new first values for each previous sequence
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])

    # The new left-most history value is the first element of the original sequence
    return sequences[0][0]

# Example data
data = []

data12 = open("input09.txt", "r").readlines()

for line in data12:
    new_line = list(map(int ,line.strip().split(' ')))
    print(new_line)
    data.append(new_line)

# Calculating the sum of extrapolated previous values
sum_of_extrapolated_previous_values = sum(extrapolate_previous_value(history) for history in data)
print("Part 2:", sum_of_extrapolated_previous_values)
