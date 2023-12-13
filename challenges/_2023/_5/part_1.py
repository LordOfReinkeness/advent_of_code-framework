from challenges._2023._5.input_parse import parse_input


def main(data):
    seeds, maps, greatest = parse_input(data)
    # Your challenges for AOC 2023 day 5 part 1 goes here

    for conversions in maps:
        for i in range(len(seeds)):
            for conversion in conversions[1]:
                if seeds[i] in range(conversion[1], conversion[1] + conversion[2]):
                    seeds[i] = conversion[0] + (seeds[i] - conversion[1])
                    break

    seeds.sort()

    return seeds[0]
