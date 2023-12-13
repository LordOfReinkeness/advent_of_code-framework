def parse_input(data):
	out = []
	# Your challenges for AOC 2023 day 4 input parsing goes here
	for row in data.split('\n')[:-1]:
		card = row.split(': ')[1].split(' | ')
		winning_numbers = card[0].split(' ')
		your_numbers = card[1].split(' ')

		while '' in winning_numbers:
			winning_numbers.remove('')

		while '' in your_numbers:
			your_numbers.remove('')

		for i in range(len(winning_numbers)):
			winning_numbers[i] = int(winning_numbers[i])

		for i in range(len(your_numbers)):
			your_numbers[i] = int(your_numbers[i])

		out.append([winning_numbers, your_numbers])

	return out
