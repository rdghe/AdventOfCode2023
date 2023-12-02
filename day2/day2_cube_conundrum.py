import re


class CubeReveal:
    def __init__(self, red_cubes: int, green_cubes: int, blue_cubes: int) -> None:
        self.red_cubes = red_cubes
        self.green_cubes = green_cubes
        self.blue_cubes = blue_cubes

    def __str__(self) -> str:
        return f'Red cubes: {self.red_cubes}\nGreen cubes: {self.green_cubes}\nBlue cubes: {self.blue_cubes}'


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


def main():
    total = 0

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
                print(cube_reveal.strip())
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
            print(f'Game with ID {cube_conundrum.game_id} is {cube_conundrum.validate_cube_reveals()}')
            if cube_conundrum.validate_cube_reveals():
                total += cube_conundrum.game_id

            print('##########')

    print(f'{total}')


if __name__ == "__main__":
    main()
