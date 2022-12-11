from pathlib import Path
from re import match


def parse_input(_input: str) -> tuple[dict, list]:

    move_lines = []
    crate_lines = []

    # process lines as crates until we reach moves section
    for line in _input.splitlines():
        if line.startswith("move"):
            move_lines.append(line)
            continue

        if "[" in line:

            crate_lines.insert(0, line)
            continue

        if line.replace(" ", "").isdigit():
            # assume stack number is single digit (i.e. 1 - 9)
            columns = {
                int(stack): column
                for column, stack in enumerate(line)
                if stack.isdigit()
            }
            continue

    stacks = build_stacks(columns, crate_lines)
    moves = [build_move(line) for line in move_lines]

    return stacks, moves


def build_stacks(columns, rows):
    stacks = {}
    # put crates into stacks
    for row in rows:
        for stack_number, column in columns.items():
            if crate := row[column].strip():
                stacks.setdefault(stack_number, []).append(crate)

    return stacks


def build_move(move_line: str):
    m = match(r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)", move_line)
    return {key: int(value) for key, value in m.groupdict().items()}


def part1(_input):
    stacks, moves = parse_input(_input)
    return simulate(stacks, moves, cratemover9000)


def part2(_input):
    stacks, moves = parse_input(_input)
    return simulate(stacks, moves, cratemover9001)


def simulate(stacks, moves, crane):

    for move in moves:
        crane(stacks, move)
    tops = [stack[-1] for stack in stacks.values()]

    return "".join(tops)


def cratemover9000(stacks, move):
    count = move["count"]

    while count:
        stacks[move["to"]].append(stacks[move["from"]].pop())
        count -= 1


def cratemover9001(stacks: dict[int, list], move):
    count = move["count"]
    from_stack = stacks[move["from"]]
    stacks[move["from"]] = from_stack[: -1 * count]
    stacks[move["to"]].extend(from_stack[-1 * count :])


def get_input():
    with Path(__file__).parent.joinpath("input.txt").open() as _file:
        _input = _file.read()

    return _input


if __name__ == "__main__":

    input_ = get_input()
    print(part1(input_))
    print(part2(input_))
