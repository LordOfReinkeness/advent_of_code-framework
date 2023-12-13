def parse_input(data):
	out = []
	# Your challenges for AOC 2023 day 2 input parsing goes here
	dat = data.split('\n')[:-1]
	for d in dat:
		tmp = []

		game = d.split(': ')[1].split('; ')
		for game_round in game:
			round_dict = {
				'blue': 0,
				'green': 0,
				'red': 0
			}

			colors = game_round.split(', ')
			for color in colors:
				color = color.split(' ')
				round_dict[color[1]] = int(color[0])

			tmp.append(round_dict)

		out.append(tmp)

	return out
