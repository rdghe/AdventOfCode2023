import re


class CubeReveal:
    def __init__(self, red_cubes: int, green_cubes: int, blue_cubes: int) -> None:
        self.red_cubes = red_cubes
        self.green_cubes = green_cubes
        self.blue_cubes = blue_cubes

    def __str__(self) -> str:
        return f'Red cubes: {self.red_cubes}; Green cubes: {self.green_cubes}; Blue cubes: {self.blue_cubes}'


class CubeConundrum:
    def __init__(self, game_id: int, cube_reveals: list[CubeReveal]) -> None:
        self.game_id = game_id
        self.max_red_cubes = 12
        self.max_green_cubes = 13
        self.max_blue_cubes = 14
        self.cube_reveals = cube_reveals

    def validate_cube_reveal(self, cube_reveal: CubeReveal) -> bool:
        """
        Validate the cube reveal
        """
        return (
                cube_reveal.red_cubes <= self.max_red_cubes and
                cube_reveal.green_cubes <= self.max_green_cubes and
                cube_reveal.blue_cubes <= self.max_blue_cubes
        )

    def validate_cube_reveals(self) -> bool:
        """
        Validate all cube reveals
        """
        for cube_reveal in self.cube_reveals:
            if not self.validate_cube_reveal(cube_reveal):
                return False
        return True

    def calculate_minimum_cubes(self) -> list[int]:
        """
        Calculate the minimum number of cubes for each color
        """
        max_revealed_red_cubes = max(
            [cube_reveal.red_cubes for cube_reveal in self.cube_reveals] + [0]  # 0 is the minimum
        )
        max_revealed_green_cubes = max(
            [cube_reveal.green_cubes for cube_reveal in self.cube_reveals] + [0]  # 0 is the minimum
        )
        max_revealed_blue_cubes = max(
            [cube_reveal.blue_cubes for cube_reveal in self.cube_reveals] + [0]  # 0 is the minimum
        )

        return [max_revealed_red_cubes, max_revealed_green_cubes, max_revealed_blue_cubes]


def main():
    sum_of_game_ids = 0
    sum_of_power_set_of_cubes = 0

    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

        for line in data:
            print(line.strip())
            game, cube_reveals = line.split(':', 1)
            game_id = int(game.split(' ')[1])
            cube_reveals = cube_reveals.split(';')
            cube_reveal_objects = []

            for cube_reveal in cube_reveals:
                # Split the cube reveal into its components and construct CubeReveal objects
                # Each cube reveal may reveal information about multiple colors, but not necessarily all three
                # Use a regex with 3 capturing groups to extract the number of cubes revealed for each color
                red_cube_search = re.compile(r'(\d+) red').search(cube_reveal)
                green_cube_search = re.compile(r'(\d+) green').search(cube_reveal)
                blue_cube_search = re.compile(r'(\d+) blue').search(cube_reveal)
                red_cubes = int(red_cube_search.group(1)) if red_cube_search else 0
                green_cubes = int(green_cube_search.group(1)) if green_cube_search else 0
                blue_cubes = int(blue_cube_search.group(1)) if blue_cube_search else 0

                cube_reveal = CubeReveal(red_cubes, green_cubes, blue_cubes)
                print(cube_reveal)
                cube_reveal_objects.append(cube_reveal)

            cube_conundrum = CubeConundrum(game_id, cube_reveal_objects)
            print(f'Game with ID {cube_conundrum.game_id} is '
                  f'{"valid" if cube_conundrum.validate_cube_reveals() else "invalid"}')
            if cube_conundrum.validate_cube_reveals():
                sum_of_game_ids += cube_conundrum.game_id

            minimum_cubes = cube_conundrum.calculate_minimum_cubes()
            sum_of_power_set_of_cubes += minimum_cubes[0] * minimum_cubes[1] * minimum_cubes[2]
            print(f'Minimum number of cubes for each color: {minimum_cubes[0]} red, '
                  f'{minimum_cubes[1]} green, {minimum_cubes[2]} blue')

            print('\n\n')

    print(f'The answer to part 1 (sum of Game IDs) is: {sum_of_game_ids}')
    print(f'The answer to part 2 (sum of power set of cubes) is: {sum_of_power_set_of_cubes}')


if __name__ == "__main__":
    main()
