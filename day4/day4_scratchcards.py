import re
from collections import defaultdict


def main():
    total_score = 0
    scratchcards_won = defaultdict(int)

    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    for index, line in enumerate(data):
        card_info, numbers = line.strip().split(':', 1)
        card_id = int(card_info.rsplit(' ', 1)[-1])
        print(f'Card ID: {card_id}')
        winning_numbers, drawn_numbers = numbers.split('|', 1)
        winning_numbers = list(map(int, re.findall(r'\d+', winning_numbers)))
        drawn_numbers = list(map(int, re.findall(r'\d+', drawn_numbers)))
        print(f'Winning numbers: {winning_numbers}')
        print(f'Drawn numbers: {drawn_numbers}')
        # Calculate how many drawn numbers match the winning numbers
        matches = len(set(winning_numbers).intersection(set(drawn_numbers)))
        print(f'Matches: {set(winning_numbers).intersection(set(drawn_numbers))}; total: {matches}')

        # Calculate the score. The first match makes the card worth one point
        # and each match after the first doubles the point value of that card.
        score = 0
        if matches > 0:
            score += 1
        for i in range(1, matches):
            score *= 2
        print(f'Score: {score}')
        total_score += score

        # Calculate how many scratchcards are won, based on previously won scratchcards
        scratchcards_won[index] += 1
        for j in range(index + 1, index + matches + 1):
            scratchcards_won[j] += scratchcards_won[index]

        print(f'Scratchcards won: {scratchcards_won}')

        print('\n')

    print(f'Total score: {total_score}')
    print(f'Total scratchcards won: {sum([scratchcard for scratchcard in scratchcards_won.values()])}')


if __name__ == '__main__':
    main()
