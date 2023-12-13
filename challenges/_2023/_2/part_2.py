from challenges._2023._2.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2023 day 2 part 2 goes here
	out = 0

	for game in data:
		min_cubes = {
			'red': 0,
			'green': 0,
			'blue': 0
		}

		for game_round in game:
			min_cubes['red'] = max(min_cubes['red'], game_round['red'])
			min_cubes['green'] = max(min_cubes['green'], game_round['green'])
			min_cubes['blue'] = max(min_cubes['blue'], game_round['blue'])

		out += (min_cubes['red'] * min_cubes['green'] * min_cubes['blue'])

	return out
