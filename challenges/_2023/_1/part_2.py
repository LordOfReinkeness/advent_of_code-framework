from challenges._2023._1.input_parse import parse_input


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2023 day 1 part 2 goes here
    out = 0

    substrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                  'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    translations = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1,
                    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9}

    for d in data:
        firsts = {}

        # find first occurrence of on of the substrings in d and print it and its index
        for s in substrings:
            if s in d:
                firsts[s] = d.index(s)

        # find the smallest index in firsts and its value
        smallest = min(firsts.values())
        smallest_key = [k for k, v in firsts.items() if v == smallest]

        # find last occurrence of on of the substrings in d and print it and its index
        lasts = {}

        for s in substrings:
            if s in d:
                lasts[s] = d.rindex(s)

        # find the largest index in lasts and its value
        largest = max(lasts.values())
        largest_key = [k for k, v in lasts.items() if v == largest]

        # find the number in between the two substrings
        number = int(str(translations[smallest_key[0]]) + str(translations[largest_key[0]]))
        out += number

    return out
