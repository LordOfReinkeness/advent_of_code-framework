from challenges._2023._1.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2023 day 1 part 1 goes here
	out = 0

	for d in data:
		number = ''
		i = 0
		while not d[i].isnumeric():
			i += 1

		number += d[i]

		i = len(d) - 1
		while not d[i].isnumeric():
			i -= 1

		number += d[i]

		out += int(number)

	return out
