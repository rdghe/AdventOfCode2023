EXPAND_UNIT = 999999


def print_galaxy(galaxy):
    # Make the above a one-liner
    print('\n'.join([''.join(row) for row in galaxy]))


def calculate_distances(galaxies):
    distances = []
    # Find the shortest path between pairs of galaxies.
    # The distance is measured in steps, where a step is a single unit in any direction.
    for index, galaxy in enumerate(galaxies):
        # Find the shortest path between the current galaxy and all other galaxies
        for other_galaxy in galaxies[index+1:]:
            shortest_path = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
            print(f'Shortest path between {galaxy} and {other_galaxy} is {shortest_path}')
            distances.append(shortest_path)
    return distances

def main():
    with open('input.txt', 'r') as f:
        galaxy = [[num for num in line.strip()] for line in f]

    print_galaxy(galaxy)

    rows_to_expand = [row for row in range(len(galaxy)) if all(element == '.' for element in galaxy[row])]
    print(f'Rows to expand: {rows_to_expand}')
    columns_to_expand = [column for column in range(len(galaxy[0])) if all(row[column] == '.' for row in galaxy)]
    print(f'Columns to expand: {columns_to_expand}')

    # For part 1 use an EXPAND_UNIT of 1; for part 2 use an EXPAND_UNIT of 999999
    galaxies = [
        (
            row_index + EXPAND_UNIT * sum(row_index > row for row in rows_to_expand),
            column_index + EXPAND_UNIT * sum(column_index > column for column in columns_to_expand)
        )
        for row_index, row in enumerate(galaxy)
        for column_index, element in enumerate(row)
        if element == '#'
    ]
    print(f'Galaxies: {galaxies}')

    distances = calculate_distances(galaxies)

    print(f'Distances: {distances}')
    print(f'There are {len(distances)} pairs of galaxies, with a total distance of {sum(distances)}')


if __name__ == "__main__":
    main()
