def construct_trapezoid(values):
    """
    The trapezoid is a matrix of N*len(values) dimensions
    The first row is the `values` list.
    The second row is the difference between each value and the next one from the first row .
    The third row is the difference between each value and the next one from the second row, and so on.
    The last row will always be a row of zeros.
    :param values: The list of values to construct the trapezoid from
    :return: The trapezoid matrix
    """
    # Initialize the trapezoid with the first row
    trapezoid = [values]

    def compute_next_row(row):
        return [(j-i) for i, j in zip(row[:-1], row[1:])]

    current_row = values
    while not all(value == 0 for value in current_row):
        current_row = compute_next_row(current_row)
        trapezoid.append(current_row)

    return trapezoid


def find_next_element(trapezoid):
    # Loop through the rows of the trapezoid starting from the second-to-last row and moving up
    for index in range(len(trapezoid) - 2, -1, -1):
        # Append the sum of the last element in the current row and the last element in the next row
        trapezoid[index].append(trapezoid[index][-1] + trapezoid[index + 1][-1])

    return trapezoid[0][-1]


def find_previous_element(trapezoid):
    # Loop through the rows of the trapezoid starting from the second-to-last row and moving up
    for index in range(len(trapezoid) - 2, -1, -1):
        # Add the left of the array the difference between the first element
        # in the current row and the first element in the next row
        trapezoid[index].insert(0, trapezoid[index][0] - trapezoid[index + 1][0])

    return trapezoid[0][0]


def main():
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    next_elements = []
    previous_elements = []

    for line in data:
        values = list(map(int, line.split()))
        print(values)
        trapezoid = construct_trapezoid(values)
        print(trapezoid)

        next_element = find_next_element(trapezoid)
        print(f'Next element: {next_element}')
        next_elements.append(next_element)

        previous_element = find_previous_element(trapezoid)
        print(f'Previous element: {previous_element}')
        previous_elements.append(previous_element)
        print('\n')

    print(f'Sum of next elements: {sum(next_elements)}')
    print(f'Sum of previous elements: {sum(previous_elements)}')


if __name__ == '__main__':
    main()
