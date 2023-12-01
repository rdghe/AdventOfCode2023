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


def extract_calibration_value(line):
    print(f'Extracting calibration value from {line.strip()}')
    digit_ids = [i for i in range(0, len(line)) if line[i].isdigit()]
    first_digit = line[digit_ids[0]]
    last_digit = line[digit_ids[-1]]
    calibration_value = int(first_digit + last_digit)
    print(f'Calibration value: {calibration_value}\n')
    return calibration_value


def substitute_encoded_digits(line):
    print(f'Substituting encoded digits in "{line.strip()}"')
    # Iterate through groups of 5 characters in the line
    for i in range(0, len(line) - 4):
        line_part = line[i:i + 5]
        if len(line_part) < 3:
            continue
        # Replace letters with encoded digits
        for key, value in letters_to_digits.items():
            new_line_part = line_part.replace(key, value)
            if new_line_part != line_part:
                line = line[:i] + new_line_part + line[i + 5:]
                break
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

    print(total)


if __name__ == "__main__":
    main()
