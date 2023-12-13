def parse_input(data):
	out = []
	# Your challenges for AOC 2019 day 2 input parsing goes here
	for i in data.split(','):
		out.append(int(i))

	return out
