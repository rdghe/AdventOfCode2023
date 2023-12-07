CARD_COUNTS = {
    'A': 0,
    'K': 0,
    'Q': 0,
    'J': 0,
    'T': 0,
    '9': 0,
    '8': 0,
    '7': 0,
    '6': 0,
    '5': 0,
    '4': 0,
    '3': 0,
    '2': 0
}

CARD_PRIORITIES = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13
}

HAND_TYPES_PRIORITY = {
    'Five of a kind': 1,
    'Four of a kind': 2,
    'Full house': 3,
    'Three of a kind': 4,
    'Two pair': 5,
    'One pair': 6,
    'High card': 7
}


def find_hand_type(card_counts):
    """
    Find the hand type for the given cards. The types are:
    - Five of a kind, where all five cards have the same label: AAAAA
    - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    - High card, where all cards' labels are distinct: 23456
    :param card_counts: A dictionary indicating the number of cards of each type
    :return: The hand type
    """

    # Five of a kind
    if 5 in card_counts.values():
        return 'Five of a kind'

    # Four of a kind
    if 4 in card_counts.values():
        return 'Four of a kind'

    # Full house
    if 3 in card_counts.values() and 2 in card_counts.values():
        return 'Full house'

    # Three of a kind
    if 3 in card_counts.values():
        return 'Three of a kind'

    # Two pair
    if list(card_counts.values()).count(2) == 2:
        return 'Two pair'

    # One pair
    if 2 in card_counts.values():
        return 'One pair'

    # High card
    return 'High card'


def main():
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    hands = []

    for line in data:
        cards, bid = line.strip().split(' ')
        # hands['cards'] = cards
        # hands['bid'] = int(bid)

        print(f'Cards: {cards}, bid: {bid}')
        card_counts = CARD_COUNTS.copy()
        for card in cards:
            card_counts[card] += 1
        print(f'Card counts: {card_counts}')

        hand_type = find_hand_type(card_counts)
        print(f'Hand type: {hand_type}')

        hands.append((cards, int(bid), hand_type))

        print('\n')

    print(f'Hands: {hands}')
    # Order hands by the priority of their hand type, then by the card priority from left to right
    hands.sort(key=lambda hand_to_sort: (
        HAND_TYPES_PRIORITY[hand_to_sort[2]],
        CARD_PRIORITIES[hand_to_sort[0][0]],
        CARD_PRIORITIES[hand_to_sort[0][1]],
        CARD_PRIORITIES[hand_to_sort[0][2]],
        CARD_PRIORITIES[hand_to_sort[0][3]],
        CARD_PRIORITIES[hand_to_sort[0][4]]
    ))

    # Calculate the hand rank for each hand and add it to the tuple
    hands_len = len(hands)
    for index, hand in enumerate(hands):
        hand_rank = hands_len - index
        hands[index] = hand + (hand_rank,)

    print(f'Ordered hands: {hands}')

    # The answer is the sum of the product between the bid and the hand rank for each hand
    answer = sum([hand[1] * hand[3] for hand in hands])
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
