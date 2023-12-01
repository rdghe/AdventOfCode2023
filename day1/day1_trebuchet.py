letters_to_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def findall(a_str, sub):
    """
    Find all occurrences of a substring in a string
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def extract_calibration_value(line):
    """
    Extract the calibration value from a line
    """
    print(f'Extracting calibration value from {line.strip()}')
    digit_ids = [i for i in range(0, len(line)) if line[i].isdigit()]
    first_digit = line[digit_ids[0]]
    last_digit = line[digit_ids[-1]]
    calibration_value = int(first_digit + last_digit)
    print(f'Calibration value: {calibration_value}\n')
    return calibration_value


def substitute_encoded_digits(line):
    """
    Substitute encoded digits with their actual values
    """
    print(f'Substituting encoded digits in "{line.strip()}"')
    # Populate with initial digits and their indices
    digits_with_index = {i: line[i] for i in range(0, len(line)) if line[i].isdigit()}
    # Iterate through encoded digits
    for key, value in letters_to_digits.items():
        found_indexes = findall(line, key)
        if found_indexes:
            for found_index in found_indexes:
                # Add the encoded digit to the dictionary
                print(f'Found {key} in {line.strip()} at index {found_index}')
                digits_with_index[found_index] = value

    # Sort the dictionary by index
    digits_with_index = {k: v for k, v in sorted(digits_with_index.items(), key=lambda item: item[0])}
    print(f'Found digits with index: {digits_with_index}')
    # Replace the digits in the line
    for index, digit in digits_with_index.items():
        line = line[:index] + digit + line[index + 1:]

    print(f'New line: "{line.strip()}"')
    return line


def main():
    total = 0

    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()
        # Loop through each line
        for line in data:
            line = substitute_encoded_digits(line)

            # Extract the calibration value
            calibration_value = extract_calibration_value(line)
            total += calibration_value

    print(f'The sum of all calibration values is {total}')


if __name__ == "__main__":
    main()
