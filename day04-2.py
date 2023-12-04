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


def count_matches(card):
    """Count the number of matches in a card."""
    winning_numbers, player_numbers = card.split(":")[1].split(" | ")
    winning_numbers = set(map(int, winning_numbers.split()))
    player_numbers = list(map(int, player_numbers.split()))

    matches = 0
    for num in player_numbers:
        if num in winning_numbers:
            matches += 1
    return matches


def process_scratchcards(cards):
    """Process the scratchcards according to the new rules."""
    total_cards = len(cards)  # Start with the original number of cards
    card_copies = [1] * len(cards)  # Each card starts with 1 copy (itself)

    for i in range(len(cards)):
        matches = count_matches(cards[i])
        # For each match, add a copy of each following card
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    # Sum up all the copies
    total_cards = sum(card_copies)
    return total_cards

total_scratchcards = process_scratchcards(cards_data)
print("Part 2:", total_scratchcards)

