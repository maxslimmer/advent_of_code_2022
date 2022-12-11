from pathlib import Path


def part1(input_: str):

    for index in range(len(input_) - 1):
        if len(set(input_[index : index + 4])) == 4:
            return index + 4
    return None


def part2(input_: str):
    for index in range(len(input_) - 1):
        if len(set(input_[index : index + 14])) == 14:
            return index + 14
    return None


def get_input():
    with Path(__file__).parent.joinpath("input.txt").open() as file_:
        input_ = file_.read()

    return input_


if __name__ == "__main__":

    input_ = get_input()
    print(part1(input_))
    print(part2(input_))
