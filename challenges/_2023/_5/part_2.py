from challenges._2023._5.input_parse import parse_input


def main(data):
    seeds, maps, greatest = parse_input(data)
    # Your challenges for AOC 2023 day 5 part 1 goes here

    out = greatest
    tmp = 0

    for i in range(int(len(seeds) / 2)):
        for j in range(seeds[i * 2], seeds[i * 2] + seeds[(i * 2) + 1]):

            seed = j

            for conversions in maps:
                for conversion in conversions[1]:

                    if seed in range(conversion[1], conversion[1] + conversion[2]):
                        seed = conversion[0] + (seed - conversion[1])
                        break

            out = min(out, seed)

            if tmp % 10000 == 0:
                # print('{}%'.format(round(tmp / 2305286101, 5) * 100), end='\r')
                print('{}%'.format(int(round(tmp/2305286101, 5) * 10000) / 100), end='\r', flush=True)
            tmp += 1

    return out
