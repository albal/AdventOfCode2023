def navigate_to_ZZZ(instructions, node_definitions):
    # Parse the node definitions into a dictionary
    nodes = {node.split(" = ")[0]: tuple(node.split(" = ")[1].strip("()").split(", ")) for node in node_definitions}

    # Convert the instructions into a list of 0s and 1s (0 for 'L', 1 for 'R')
    instruction_indices = [0 if inst == 'L' else 1 for inst in instructions]

    # Start at 'AAA' and navigate until 'ZZZ' is reached
    current_node = 'AAA'
    steps = 0
    instruction_index = 0
    while current_node != 'ZZZ':
        # Follow the instruction
        current_node = nodes[current_node][instruction_indices[instruction_index]]
        steps += 1

        # Move to the next instruction, looping back if necessary
        instruction_index = (instruction_index + 1) % len(instruction_indices)

    return steps

# Test the function with the provided examples
instructions1 = "RL"
node_definitions1 = ["AAA = (BBB, CCC)", "BBB = (DDD, EEE)", "CCC = (ZZZ, GGG)", "DDD = (DDD, DDD)", "EEE = (EEE, EEE)", "GGG = (GGG, GGG)", "ZZZ = (ZZZ, ZZZ)"]

instructions2 = "LLR"
node_definitions2 = ["AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]

with open("input08.txt") as f:
    data = f.read().splitlines()

instructions2 = data[0]
node_definitions2 = data[2:]

print(instructions2)
print(node_definitions2)


steps1 = navigate_to_ZZZ(instructions1, node_definitions1)
steps2 = navigate_to_ZZZ(instructions2, node_definitions2)


print("Part 1: ", steps2)
