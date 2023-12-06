def main():
    solve(part=1)
    solve(part=2)


def solve(part=1):
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    times = [int(num) for num in data[0].split()[1:]]
    print(f"Times: {times}")
    record_distances = [int(num) for num in data[1].split()[1:]]
    print(f"Record distances: {record_distances}")

    if part == 2:
        # Make a single time number by concatenating the times
        times = [int(''.join([str(num) for num in times]))]
        record_distances = [int(''.join([str(num) for num in record_distances]))]

    time_and_record_distance = list(zip(times, record_distances))
    print(f"Time and distance: {time_and_record_distance}")

    number_of_winning_distances_per_race = []

    for index, (time, record_distance) in enumerate(time_and_record_distance):
        print(f'Race number {index + 1}')

        winning_distances = []
        print(f"Time: {time}, record distance: {record_distance}")
        for held_time, distance in generate_time_and_distance(time):
            if distance > record_distance:
                winning_distances.append(distance)
                print(f"Winning distance: {distance} by holding the button down for {held_time} seconds")

        print(f"Winning distances: {winning_distances}")
        number_of_winning_distances_per_race.append(len(winning_distances))

        print('\n')

    print(f'Numbers of winning distances per race {number_of_winning_distances_per_race}')

    # Multiply all list elements together
    def product_recursive(numbers):
        # base case: list is empty
        if not numbers:
            return 1
        # recursive case: multiply first element by product of the rest of the list
        return numbers[0] * product_recursive(numbers[1:])

    print(f'Problem answer: {product_recursive(number_of_winning_distances_per_race)}')


def generate_time_and_distance(max_time):
    initial_max_time = max_time
    while max_time >= 0:
        print(f'Holding the button down for {max_time} seconds')
        yield max_time, max_time * (initial_max_time - max_time)
        max_time -= 1


if __name__ == '__main__':
    main()
