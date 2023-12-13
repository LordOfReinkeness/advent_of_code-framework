from challenges._2023._3.input_parse import parse_input


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2023 day 3 part 2 goes here
	out = 0
	gears = {}

	for i in range(len(data)):
		j = -1
		while j < len(data[i]) - 1:
			j += 1

			if data[i][j].isnumeric():
				pos, next_to_gear = check_adjacent(data, i, j)
				if next_to_gear:

					if pos not in gears:
						gears[pos] = []

					number, j = find_number(data[i], j)

					gears[pos].append(number)

	for key in gears:
		if len(gears[key]) == 2:
			out += (gears[key][0] * gears[key][1])

	return out


def check_adjacent(data, y, x):
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

	for i in range(0 if y - 1 < 0 else y - 1, y + 1 if y + 1 >= len(data) else y + 2):
		for j in range(0 if x - 1 < 0 else x - 1, x + 1 if x + 1 >= len(data[i]) else x + 2):
			if data[i][j] == '*':
				return '{}:{}'.format(i, j), True

	return '-1:-1', False


def find_number(row, j):
	while j - 1 >= 0 and row[j - 1].isnumeric():
		j -= 1

	start_index = j

	while j + 1 < len(row) and row[j + 1].isnumeric():
		j += 1

	end_index = j + 1
	num = int(row[start_index:end_index])
	return num, end_index
