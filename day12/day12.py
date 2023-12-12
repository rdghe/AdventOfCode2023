def compute_possibilities(damaged_record):
    # Each damaged record contains some `?` characters that can be either `.` or `#`. We compute all possibilities
    possibilities = []
    unknowns = damaged_record.count('?')
    for i in range(2 ** unknowns):
        combinations = list(bin(i)[2:].zfill(unknowns))
        possibilities.append(
            damaged_record.replace('?', '{}').format(
                *combinations
            ).replace('0', '.').replace('1', '#')
        )

    return possibilities


def validate_possibilities(possibilities, contiguous_group):
    """
    We validate the possibilities by checking if the contiguous group is present in the possibilities.
    The contiguous group is a list of integers that represent the distribution of `#` elements. A value of 1 means that the `#` element is surrounded by `.` elements or at the beginning/end of the string, whereas values of 2 or more indicate repeated `#` elements.
    :param possibilities: The list of possibilities to validate
    :param contiguous_group: The contiguous group to validate
    :return:
    """
    valid_possibilities = []
    for possibility in possibilities:
        # print(f'Possibility: {possibility}')
        # Extract lengths of groups of `#` elements
        groups = list(map(len, possibility.split('.')))
        # print(f'Groups: {groups}')
        # Remove empty groups
        groups = [g for g in groups if g > 0]
        # print(f'Non-empty groups: {groups}')
        # Check if the groups match the contiguous group
        if groups == contiguous_group:
            valid_possibilities.append(possibility)

    return valid_possibilities


def main():
    with open('input.txt', 'r') as f:
    # with open('test_input.txt', 'r') as f:
        data = f.readlines()

    total_valid_possibilities = 0
    for line in data:
        damaged_record, contiguous_group = line.split(' ', 1)
        print(f'Damaged record: {damaged_record}')
        contiguous_group = list(map(int, contiguous_group.strip().split(',')))
        print(f'Contiguous group: {contiguous_group}')

        possibilities = compute_possibilities(damaged_record)
        print(f'Possibilities: {possibilities}')

        valid_possibilities = validate_possibilities(possibilities, contiguous_group)
        print(f'Valid possibilities: {valid_possibilities}')

        print(f'Number of valid possibilities: {len(valid_possibilities)}')
        total_valid_possibilities += len(valid_possibilities)
        print('\n')

    print(f'Total number of valid possibilities: {total_valid_possibilities}')


if __name__ == "__main__":
    main()
