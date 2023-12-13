from challenges._2023._4.input_parse import parse_input


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2023 day 4 part 2 goes here
    out = 0
    scratchcards = [1] * len(data)

    for i in range(len(data)):
        winning = []
        for number in data[i][1]:
            if number in data[i][0]:
                winning.append(number)

        new_cards = len(winning)

        for j in range(i + 1, i + 1 + new_cards):
            scratchcards[j] += scratchcards[i]

    for i in scratchcards:
        out += i

    return out
