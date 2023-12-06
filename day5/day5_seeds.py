import re
from math import inf


def main():
    min_location = inf

    # with open('test_input.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.read()

    # Define a pattern to extract values for each category with multiline matching
    pattern = re.compile(
        r'(?:(seeds):([\s\d]+\d)|(\w+-to-\w+\s+map):([\s\d]+\d)(?:\s+([\s\d]+\d))?(?:\s+([\s\d]+\d))?)'
    )

    # Create a dictionary to store the extracted data
    data_dict = {}

    # Iterate through matches and organize data into a nested structure
    for match in pattern.finditer(data):
        category = match.group(1) or match.group(3)
        values = [int(num) for num in (match.group(2) or match.group(4)).split() if num]

        if category == 'seeds':
            data_dict[category] = values
        else:
            category = category.strip().split(' ', 1)[0].replace('-', '_')
            print(category)
            # Take groups of 3 from the values list and create lists
            # of `destination_range`, `source_range` and `range_length`
            data_dict[category] = [values[i:i + 3] for i in range(0, len(values), 3)]

    print('destination range, source range, range length')
    # Print the extracted data
    for category, values in data_dict.items():
        print(f"{category}: {values}")

    # Transform seeds to ranges; e.g. [79, 14, 55, 13] becomes 79 to 93 and 55 to 68
    seeds_aux = []
    for range_start, range_end in zip(data_dict['seeds'][::2], data_dict['seeds'][1::2]):
        print(f"{range_start} to {range_start + range_end}")
        seeds_aux.append(range(range_start, range_start + range_end))

    data_dict['seeds'] = seeds_aux
    print(f"Seeds: {data_dict['seeds']}")
    print(f'Seeds length: {len(data_dict["seeds"])}')

    # Map the seeds to soil and all the way to location
    for seed_range in data_dict['seeds']:
        print(f"Seed range: {seed_range}")
        for seed in seed_range:
            soil = map_seed_to_soil(seed, data_dict['seed_to_soil'])
            fertilizer = map_soil_to_fertilizer(soil, data_dict['soil_to_fertilizer'])
            water = map_fertilizer_to_water(fertilizer, data_dict['fertilizer_to_water'])
            light = map_water_to_light(water, data_dict['water_to_light'])
            temperature = map_light_to_temperature(light, data_dict['light_to_temperature'])
            humidity = map_temperature_to_humidity(temperature, data_dict['temperature_to_humidity'])
            location = map_humidity_to_location(humidity, data_dict['humidity_to_location'])

            # Store the answer: the minimum location
            if location < min_location:
                min_location = location

    print(f"Minimum location: {min_location}")


def map_seed_to_soil(seed, seed_to_soil_map):
    # Map the seed to a soil based on the seed_to_soil_map
    for destination_range, source_range, range_length in seed_to_soil_map:
        if seed in range(source_range, source_range + range_length):
            return seed + destination_range - source_range

    return seed


def map_soil_to_fertilizer(soil, soil_to_fertilizer_map):
    # Map the soil to a fertilizer based on the soil_to_fertilizer_map
    for destination_range, source_range, range_length in soil_to_fertilizer_map:
        if soil in range(source_range, source_range + range_length):
            return soil + destination_range - source_range

    return soil


def map_fertilizer_to_water(fertilizer, fertilizer_to_water_map):
    # Map the fertilizer to water based on the fertilizer_to_water_map
    for destination_range, source_range, range_length in fertilizer_to_water_map:
        if fertilizer in range(source_range, source_range + range_length):
            return fertilizer + destination_range - source_range

    return fertilizer


def map_water_to_light(water, water_to_light_map):
    # Map the water to light based on the water_to_light_map
    for destination_range, source_range, range_length in water_to_light_map:
        if water in range(source_range, source_range + range_length):
            return water + destination_range - source_range

    return water


def map_light_to_temperature(light, light_to_temperature_map):
    # Map the light to temperature based on the light_to_temperature_map
    for destination_range, source_range, range_length in light_to_temperature_map:
        if light in range(source_range, source_range + range_length):
            return light + destination_range - source_range

    return light


def map_temperature_to_humidity(temperature, temperature_to_humidity_map):
    # Map the temperature to humidity based on the temperature_to_humidity_map
    for destination_range, source_range, range_length in temperature_to_humidity_map:
        if temperature in range(source_range, source_range + range_length):
            return temperature + destination_range - source_range

    return temperature

def map_humidity_to_location(humidity, humidity_to_location_map):
    # Map the humidity to location based on the humidity_to_location_map
    for destination_range, source_range, range_length in humidity_to_location_map:
        if humidity in range(source_range, source_range + range_length):
            return humidity + destination_range - source_range

    return humidity


if __name__ == '__main__':
    main()
