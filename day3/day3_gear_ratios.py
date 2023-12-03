from pprint import pprint


def traverse_matrix(matrix):
    """
    Traverse the matrix and extract the numbers and special characters, together with their indices.
    :param matrix: list of lists, each list representing a row in the matrix
    :return: list of tuples, each tuple containing the number or special character, start index and end index
    """
    numbers = []
    special_characters = []
    processed_indices = set()

    for row_index, row in enumerate(matrix):
        for col_index, char in enumerate(row):
            # Check if the current index has already been processed
            if (row_index, col_index) in processed_indices:
                continue

            # Check if we encountered a special character
            if not char.isdigit() and char != '.':
                special_characters.append((char, (row_index, col_index)))
                continue

            # Check if the current character is a digit
            if char.isdigit():
                current_number = char
                current_number_start_index = (row_index, col_index)
                current_number_end_index = (row_index, col_index)
                # Continue reading to the right within matrix borders
                for next_col_index in range(col_index + 1, len(row)):
                    next_char = matrix[row_index][next_col_index]
                    if next_char.isdigit():
                        current_number += next_char
                        current_number_end_index = (row_index, next_col_index)
                        processed_indices.add((row_index, next_col_index))
                    else:
                        break  # Stop if a non-digit character is encountered
                numbers.append((int(current_number), current_number_start_index, current_number_end_index))

    # Print the numbers
    for number in numbers:
        print(f'Number: {number[0]}, start index: {number[1]}, end index: {number[2]}')
    # Print the special characters
    for special_character in special_characters:
        print(f'Special character {special_character[0]} found at '
              f'index {special_character[1][0]}, {special_character[1][1]}')

    return numbers, special_characters


def find_part_numbers(numbers, special_characters):
    """
    Numbers are considered "part numbers" if they are adjacent to at least one special
    character, either horizontally, vertically or diagonally.
    :param numbers: list of tuples, each tuple containing the number, start index and end index
    :param special_characters: list of tuples, each tuple containing the special character and its index
    :return: list of part numbers
    """
    part_numbers = []

    # Check if the special character is adjacent to the number, either horizontally, vertically or diagonally
    for number in numbers:
        for special_character in special_characters:
            # Check for horizontal adjacency
            if special_character[1][0] == number[1][0] and (
                    special_character[1][1] == number[1][1] - 1 or
                    special_character[1][1] == number[2][1] + 1
            ):
                part_numbers.append((number, special_character))
                break
            # Check for vertical adjacency
            if special_character[1][1] == number[1][1] and (
                    special_character[1][0] == number[1][0] - 1 or
                    special_character[1][0] == number[2][0] + 1
            ):
                part_numbers.append((number, special_character))
                break
            if special_character[1][1] == number[2][1] and (
                    special_character[1][0] == number[1][0] - 1 or
                    special_character[1][0] == number[2][0] + 1
            ):
                part_numbers.append((number, special_character))
                break
            # Check for diagonal adjacency
            if abs(special_character[1][0] - number[1][0]) == 1 and abs(special_character[1][1] - number[1][1]) == 1:
                part_numbers.append((number, special_character))
                break
            if abs(special_character[1][0] - number[2][0]) == 1 and abs(special_character[1][1] - number[2][1]) == 1:
                part_numbers.append((number, special_character))
                break

    # Print the part numbers
    for number in part_numbers:
        print(f'Part number: {number[0]}, adjacent to special character {number[1]}')

    return part_numbers


def find_gear_ratios(part_numbers):
    """
    Find the gear ratios for each part number.
    A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.
    :param part_numbers: list of tuples, each tuple containing the number, start index and end index
    :return: list of gear ratios
    """
    # Group the part numbers by special character
    part_numbers_by_special_character = {}
    for part_number in part_numbers:
        if part_number[1] not in part_numbers_by_special_character:
            part_numbers_by_special_character[part_number[1]] = [part_number[0]]
        else:
            part_numbers_by_special_character[part_number[1]].append(part_number[0])

    print('Part numbers grouped by special character:')
    pprint(part_numbers_by_special_character)

    # Identify the gears and calculate the gear ratios
    gear_ratios = []
    for key, value in part_numbers_by_special_character.items():
        if key[0] == '*' and len(value) == 2:
            gear_ratio = value[0][0] * value[1][0]
            print(f'Gear: {value[0][0]} with {value[1][0]}, gear ratio: {gear_ratio}')
            gear_ratios.append(gear_ratio)

    return gear_ratios


def main():
    with open('input.txt', 'r') as f:
        matrix = [list(row) for row in f.read().strip().split('\n')]

    # Traverse the matrix and extract the numbers and special characters, together with their indices
    numbers, special_characters = traverse_matrix(matrix)
    print(f'Numbers: {numbers}')
    print(f'Special characters: {special_characters}')

    # Find part numbers and calculate their sum
    part_numbers = find_part_numbers(numbers, special_characters)
    print(f'Sum of part numbers: {sum(number[0][0] for number in part_numbers)}\n\n')

    gear_ratios = find_gear_ratios(part_numbers)
    print(f'Gear ratios: {gear_ratios}')
    print(f'Sum of gear ratios: {sum(gear_ratios)}')


if __name__ == '__main__':
    main()
