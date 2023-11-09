from challenges._2019._1.input_parse import parse_input


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2019 day 1 part 1 goes here
    solution = 0

    for d in data:
        add = d // 3 - 2
        solution += add

    return solution
