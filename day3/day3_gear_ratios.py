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


def validate_numbers(numbers, special_characters):
    """
    Numbers are considered valid if they are adjacent to at least one special
    character, either horizontally, vertically or diagonally.
    :param numbers: list of tuples, each tuple containing the number, start index and end index
    :param special_characters: list of tuples, each tuple containing the special character and its index
    :return: list of valid numbers
    """
    valid_numbers = []

    # Check if the special character is adjacent to the number, either horizontally, vertically or diagonally
    for number in numbers:
        for special_character in special_characters:
            # Check for horizontal adjacency
            if special_character[1][0] == number[1][0] and (
                    special_character[1][1] == number[1][1] - 1 or
                    special_character[1][1] == number[2][1] + 1
            ):
                valid_numbers.append(number[0])
                break
            # Check for vertical adjacency
            if special_character[1][1] == number[1][1] and (
                    special_character[1][0] == number[1][0] - 1 or
                    special_character[1][0] == number[2][0] + 1
            ):
                valid_numbers.append(number[0])
                break
            if special_character[1][1] == number[2][1] and (
                    special_character[1][0] == number[1][0] - 1 or
                    special_character[1][0] == number[2][0] + 1
            ):
                valid_numbers.append(number[0])
                break
            # Check for diagonal adjacency
            if abs(special_character[1][0] - number[1][0]) == 1 and abs(special_character[1][1] - number[1][1]) == 1:
                valid_numbers.append(number[0])
                break
            if abs(special_character[1][0] - number[2][0]) == 1 and abs(special_character[1][1] - number[2][1]) == 1:
                valid_numbers.append(number[0])
                break

    # Print the valid numbers
    for number in valid_numbers:
        print(f'Valid number: {number}')

    return valid_numbers


def main():
    with open('test_input.txt', 'r') as f:
        matrix = [list(row) for row in f.read().strip().split('\n')]

    # Traverse the matrix and extract the numbers and special characters, together with their indices
    numbers, special_characters = traverse_matrix(matrix)
    print(f'Numbers: {numbers}')
    print(f'Special characters: {special_characters}')

    # Find valid numbers
    valid_numbers = validate_numbers(numbers, special_characters)

    # Calculate the gear ratio
    gear_ratio = sum(valid_numbers)
    print(f'Gear ratio: {gear_ratio}')


if __name__ == '__main__':
    main()
