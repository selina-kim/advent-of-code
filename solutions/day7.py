from icecream import ic

############# Example Part 1 #############
EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day7.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def solution(input):

    lines = input.split("\n")

    hands = [[] for _ in range(7)]

    for line_idx, line in enumerate(lines):
        cards = [x for x in line.split(" ")[0]]
        bid = int(line.split(" ")[1])
        count = {}
        # ic(cards)

        for card in cards:
            if card not in count:
                count[card] = 1
            else:
                count[card] += 1

        # ic(count)

        # five of a kind -> 0
        if len(count) == 1:
            hands[6].append([cards, bid])
        # four of a kind -> 1
        elif 4 in count.values():
            hands[5].append([cards, bid])
        # full house (3 same, 2 same) -> 2
        elif (len(count) == 2) and 3 in count.values():
            hands[4].append([cards, bid])
        # 3 of a kind (3 same, 2 diff) -> 3
        elif 3 in count.values():
            hands[3].append([cards, bid])
        # 2 pair (2 same, 2 same, 1 diff) -> 4
        elif (len(count) == 3) and 2 in count.values():
            hands[2].append([cards, bid])
        # 1 pair (2 same, 3 diff) -> 5
        elif (len(count) == 4):
            hands[1].append([cards, bid])
        # high card (all diff) -> 6
        else:
            hands[0].append([cards, bid])

    ic(hands)

    ranked = [[] for _ in range(7)]

    for type_idx, handType in enumerate(hands):
        if handType != []:
            for hand in handType:
                # ic(hand)
                if ranked[type_idx] == []:
                    ranked[type_idx].append(hand)
                else:
                    added = False
                    for comp_idx, comp in enumerate(ranked[type_idx]):
                        # ic(type_idx, hand, comp_idx, comp)
                        order = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
                        for card in range(5):
                            if order.index(comp[0][card]) < order.index(hand[0][card]):
                                ranked[type_idx].insert(comp_idx, hand)
                                added = True
                                break
                            if order.index(comp[0][card]) > order.index(hand[0][card]):
                                break
                        if added:
                            break
                        elif comp_idx == len(ranked[type_idx])-1:
                            ranked[type_idx].append(hand)
                            break
                # ic(ranked)

    # ic(ranked)

    res = 0
    rank = 1
    
    for handType in ranked:
        for hand in handType:
            res += rank * hand[1]
            rank += 1

    print(res)

    # ---------------------------------------------------------
            
    with open('testing-output/day7.txt', 'w') as f:
        f.write(str(res))
        for type_idx, handType in enumerate(ranked):
            for hand in handType:
                f.write("\n" + str(type_idx) + ": ")
                f.write(str(hand[0]))
                f.write(" - " + str(hand[1]))

    # ---------------------------------------------------------

# solution(EXAMPLE)
solution(PUZZLE)