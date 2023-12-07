def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(handtype(hand.replace('0', r)) for r in '23456789ABCDE')
    return best, hand, int(bid)


def handtype(hand):
    return sorted(map(hand.count, hand), reverse=True)


for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open('input07.txt'))), start=1)))