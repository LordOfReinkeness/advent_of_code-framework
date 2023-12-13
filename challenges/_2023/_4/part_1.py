from challenges._2023._4.input_parse import parse_input


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2023 day 4 part 1 goes here
	out = 0
	for card in data:
		winning = []
		for number in card[1]:
			if number in card[0]:
				winning.append(number)
		
		if len(winning) > 0:
			out += 2 ** (len(winning) - 1)

	return out
