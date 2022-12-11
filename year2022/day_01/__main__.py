from pathlib import Path


def elves_totals(data):

    snacks = []
    elves = [snacks]
    for line in data.splitlines():
        if line:

            snacks.append(int(line))

        else:
            snacks = []
            elves.append(snacks)

    return [sum(elf) for elf in elves]


def main(_input):

    totals = elves_totals(_input)

    totals.sort(reverse=True)
    return totals[0], sum(totals[0:3])


def get_input():
    with Path(__file__).parent.joinpath("input.txt").open() as _file:
        _input = _file.read()

    return _input


if __name__ == "__main__":

    answer_part1, answer_part2 = main(get_input())

    print(f"part 1: {answer_part1}")
    print(f"part 2: {answer_part2}")
