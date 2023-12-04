import re


def main():
    total_score = 0
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    for line in data:
        card_info, numbers = line.strip().split(':', 1)
        winning_numbers, drawn_numbers = numbers.split('|', 1)
        winning_numbers = list(map(int, re.findall(r'\d+', winning_numbers)))
        draw_numbers = list(map(int, re.findall(r'\d+', drawn_numbers)))
        print(f'Card: {card_info}, winning numbers: {winning_numbers}, draw numbers: {draw_numbers}')
        # Calculate how many drawn numbers match the winning numbers
        matches = len(set(winning_numbers).intersection(set(draw_numbers)))
        print(f'Matches: {set(winning_numbers).intersection(set(draw_numbers))}; total: {matches}')

        # Calculate the score. The first match makes the card worth one point
        # and each match after the first doubles the point value of that card.
        score = 0
        if matches > 0:
            score += 1
        for i in range(1, matches):
            score *= 2
        print(f'Score: {score}\n')

        total_score += score

    print(f'Total score: {total_score}')


if __name__ == '__main__':
    main()
