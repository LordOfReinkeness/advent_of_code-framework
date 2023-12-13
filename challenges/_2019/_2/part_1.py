from challenges._2019._2.input_parse import parse_input


def main(data):
    data = parse_input(data)
    data[1] = 12
    data[2] = 2
    # Your challenges for AOC 2019 day 2 part 1 goes here

    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[i + 3] = data[data[i + 1]] * data[data[i + 2]]
        elif data[i] == 90:
            break
        else:
            break

    return data[0]
