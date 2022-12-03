from aoc.util import get_data


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


if __name__ == "__main__":
    data = get_data(__file__)
    totals = elves_totals(data)

    totals.sort(reverse=True)
    answer_part1 = totals[0]
    answer_part2 = sum(totals[0:3])

    print(f"part 1: {answer_part1}")
    print(f"part 2: {answer_part2}")
