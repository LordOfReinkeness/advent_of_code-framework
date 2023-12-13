from challenges._2023._2.input_parse import parse_input


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2023 day 2 part 1 goes here
    out = 0
    max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for i in range(len(data)):
        possible = True

        for d in data[i]:
            if d['red'] > max_cubes['red']:
                possible = False
                break

            if d['green'] > max_cubes['green']:
                possible = False
                break

            if d['blue'] > max_cubes['blue']:
                possible = False
                break

        if possible:
            out += i + 1

    return out
