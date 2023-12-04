# First, let's parse the card data and then calculate the points for each card.

cards_data = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    " 1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

cards_data = open("input04.txt", "r").readlines()


def calculate_points(card):
    data = card.split(":")[1]
    winning_numbers, player_numbers = data.split(" | ")
    winning_numbers = set(map(int, winning_numbers.split()))
    player_numbers = list(map(int, player_numbers.split()))

    points = 0
    for num in player_numbers:
        if num in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

total_points = sum(calculate_points(card) for card in cards_data)
print("Part 1:", total_points)

