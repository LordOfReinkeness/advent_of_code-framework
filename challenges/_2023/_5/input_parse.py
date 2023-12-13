def parse_input(data):
	seeds = []
	maps = []
	greatest = 0
	# Your challenges for AOC 2023 day 5 input parsing goes here
	data = data.split('\n\n')

	for seed in data[0].split(': ')[1].split(' '):
		seeds.append(int(seed))

	for map_item in data[1:]:
		lines = map_item.split('\n')

		names = lines[0].split(' ')[0].split('-to-')
		converted_conversions = []

		for line in lines[1:]:
			converted_conversion = []
			for item in line.split(' '):
				converted_conversion.append(int(item))

			converted_conversions.append(converted_conversion)

		maps.append([names, sorted(converted_conversions, key=lambda x: x[0])])

		for i in maps:
			for j in i[1]:
				greatest = max(j[0] + j[2], greatest)
				greatest = max(j[1] + j[2], greatest)

	return seeds, maps, greatest
