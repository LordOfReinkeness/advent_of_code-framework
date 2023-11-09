from challenges._2019._1.input_parse import parse_input


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2019 day 1 part 1 goes here
	solution = 0

	for d in data:
		fuel = d // 3 - 2
		solution += fuel
		need_more = True
		while need_more:
			fuel = fuel // 3 - 2
			if fuel <= 0:
				need_more = False
			else:
				solution += fuel

	return solution
