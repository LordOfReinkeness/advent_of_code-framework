def parse_input(data):
	out = []

	data = data.split('\n')
	for d in data[:-1]:
		out.append(int(d))

	# Your challenges for AOC 2019 day 1 input parsing goes here
	return out
