import argparse
import json
import os
import sys
import datetime
import time
import markdownify
import requests
import importlib.util
from dotenv import load_dotenv


def init(day, year):
    directory = './challenges/_%s/_%s' % (year, day)
    if os.path.exists(directory):
        print('Directory already exists')
        sys.exit(1)

    os.makedirs(directory)

    if os.path.exists('./challenges/_%s/__init__.py' % year):
        f = open('./challenges/_%s/__init__.py' % year, 'w')
        f.write("")
        f.close()

    for i in range(2):
        f = open('%s/part_%s.py' % (directory, i + 1), 'x')
        f.write(
            "from challenges._%s._%s.input_parse import parse_input\n\n"
            "def main(data):"
            "\n\tdata = parse_input(data)"
            "\n\t# Your challenges for AOC %s day %s part %d goes here\n"
            "\n\treturn 'AOC %s day %s part %s'\n" %
            (year, day, year, day, i + 1, year, day, i + 1))
        f.close()

    f = open('%s/input_parse.py' % directory, 'x')
    f.write("def parse_input(data):"
            "\n\tout = data"
            "\n\t# Your challenges for AOC %s day %s input parsing goes here"
            "\n\treturn out\n" %
            (year, day))
    f.close()

    get_puzzle(1, day, year)

    f = open('%s/input.txt' % directory, 'x')
    f.write(get_from_aoc('https://adventofcode.com/%s/day/%s/input' % (year, day)))
    f.close()

    f = open('%s/testdata.txt' % directory, 'x')
    f.write("")
    f.close()

    print('Created directory %s and day files' % directory)


def run(day, year, args):
    path = './challenges/_%s/_%s' % (year, day)

    f = open('state.json')
    puzzle_state = json.load(f)
    f.close()

    if year not in puzzle_state['years']:
        print("Year not found: Could not execute")
        sys.exit(1)

    if day not in puzzle_state['years'][year]:
        print("Day not found: Could not execute")
        sys.exit(1)

    data_file = '%s/input.txt' % path

    if args.test:
        data_file = '%s/testdata.txt' % path

    with open(data_file, 'r') as f:
        data = f.read()

    if '1' in puzzle_state['years'][year][day] and puzzle_state['years'][year][day]['1'] != '':
        print('Part 1 already completed. Solution was: "%s"' % puzzle_state['years'][year][day]['1'])

        if '2' in puzzle_state['years'][year][day] and puzzle_state['years'][year][day]['2'] != '':
            print('Part 2 already completed. Solution was: "%s"' % puzzle_state['years'][year][day]['2'])
        else:
            print('Running part 2')
            solution = run_part('%s/part_2.py' % path, data)
            print('Solution: %s' % solution)
            if args.submit:
                submit(day, year, 2, solution)

    else:
        print('Running part 1')
        solution = run_part('%s/part_1.py' % path, data)
        print('Solution: %s' % solution)
        if args.submit:
            submit(day, year, 1, solution)


def submit(day, year, part, solution):
    print("Submitting solution")

    url = 'https://adventofcode.com/%s/day/%s/answer' % (year, day)
    data = {'level': part, 'answer': solution}
    session_cookie = 'session=%s' % os.getenv('SESSION_COOKIE')
    answer = requests.get(url, data, headers={'cookie': session_cookie}).text

    if "You gave an answer too recently" in answer:
        print('You gave an answer too recently')
        sys.exit(1)
    elif "That's not the right answer" in answer:
        content = markdownify.markdownify(answer.split('<article class="day-desc">')[part].split('</article>')[0])
        print('That\'s not the right answer:')
        print(content)
        sys.exit(1)
    elif "That's the right answer" in answer:
        print('That\'s the right answer!')

        with open('state.json', 'r') as f:
            puzzle_state = json.load(f)

        puzzle_state['years'][year][day][int(part)] = solution

        with open('state.json', 'w') as f:
            json.dump(puzzle_state, f, indent=2)

        if part == 1:
            get_puzzle(2, day, year)
    else:
        content = markdownify.markdownify(answer.split('<article class="day-desc">')[part].split('</article>')[0])
        print('Something went wrong:')
        print(content)
        sys.exit(1)


def run_part(path, data):
    spec = importlib.util.spec_from_file_location("module.name", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    start = time.time()
    solution = module.main(data)
    end = time.time()
    print('Took %s seconds' % (round((end - start) * 1000, 2)))
    return solution


def get_puzzle(part, day, year):
    with open('state.json', 'r') as f:
        puzzle_state = json.load(f)

    if year not in puzzle_state['years']:
        puzzle_state['years'][year] = {}

    if day not in puzzle_state['years'][year]:
        puzzle_state['years'][year][day] = {}

    if part in puzzle_state['years'][year][day]:
        print('Puzzle already fetched')
    else:
        puzzle_state['years'][year][day][part] = ''

        url = 'https://adventofcode.com/%s/day/%s' % (year, day)
        content = get_from_aoc(url)
        content = markdownify.markdownify(content.split('<article class="day-desc">')[part].split('</article>')[0])

        with open('state.json', 'w') as f:
            json.dump(puzzle_state, f, indent=2)

        f = open('./challenges/_%s/_%s/Puzzle_%d.md' % (year, day, part), 'x')
        f.write(content)
        f.close()


def get_from_aoc(url):
    session_cookie = 'session=%s' % os.getenv('SESSION_COOKIE')
    return requests.get(url, headers={'cookie': session_cookie}).text


def main(argv):
    parser = argparse.ArgumentParser(description='Advent of Code Wrapper')
    parser.add_argument('-i', '--init', action='store_true', help='Initialize a new day')
    parser.add_argument('-s', '--submit', action='store_true', help='Run and submit solution via api')
    parser.add_argument('-t', '--test', action='store_true', help='Run on test data')
    parser.add_argument('-d', '--day', help='Day to run default is today', default=datetime.datetime.today().day)
    parser.add_argument('-y', '--year', help='Year to run default is this year', default=datetime.datetime.today().year)
    args = parser.parse_args()

    load_dotenv()

    if int(args.day) > 25 or int(args.day) < 1:
        print('Invalid day')
        sys.exit(1)

    # print number of current day of the month
    if args.init:
        init(args.day, args.year)
    else:
        run(args.day, args.year, args)


if __name__ == "__main__":
    main(sys.argv)
