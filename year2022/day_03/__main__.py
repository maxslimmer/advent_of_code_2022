from year2022.util import get_input

from string import ascii_letters


def part_1():

    data = get_input(__file__)
    priorities = []
    for line in data.splitlines():
        compart1 = set(line[: len(line) // 2])
        compart2 = set(line[len(line) // 2 :])
        common = compart1.intersection(compart2).pop()
        priorities.append(ascii_letters.index(common) + 1)

    return sum(priorities)


def part_2():
    data = get_input(__file__)
    priorities = []
    for group in zip(*[iter(data.splitlines())] * 3):
        badge = (
            set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        )
        priorities.append(ascii_letters.index(badge) + 1)

    return sum(priorities)


if __name__ == "__main__":
    print(part_1())  # 7742
    print(part_2())  # 2276
