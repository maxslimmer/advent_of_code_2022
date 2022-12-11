from pprint import pprint
from year2022.util import get_input


def walk_tree(node_name, node, size, state):
    if isinstance(node, dict):
        size = 0

        for item in node.items():
            if isinstance(item[1], int):
                size += item[1]

            else:
                size += walk_tree(
                    node_name + ("" if node_name == "/" else "/") + item[0],
                    item[1],
                    size,
                    state,
                )
        state[node_name] = size
    return size


def parse_term_out(input_: str):
    files = {}
    root = {}
    fs = {"/": root}
    dirs = {"/": root}
    for line in input_.splitlines():
        output = line.split()
        match output:
            case ["$", *cmd]:
                match cmd:
                    case ["cd", "/"]:
                        stack = []
                    case ["cd", ".."]:
                        stack.pop()
                    case ["cd", directory]:
                        stack.append(directory)
                    case ["ls"]:
                        continue
                    case other:
                        ValueError(f"unknown or invalid command{' '.join(other)}")
            case ["dir", dir_name]:
                # NB Assumes we only ls once per directory
                cwd = "/" + "/".join(stack)
                path = cwd + ("/" if len(stack) else "") + dir_name
                dirs[cwd][dir_name] = dirs[path] = {}
            case [size, file_name]:
                cwd = "/" + "/".join(stack)
                path = cwd + ("/" if len(stack) else "") + file_name
                dirs[cwd][file_name] = int(size)
                files[path] = int(size)
            case other:
                ValueError(f"unknown output value {' '.join(other)}")
    return fs, dirs, files


def part1(input_: str) -> int:
    ...


if __name__ == "__main__":

    input_ = get_input(__file__)
    fs, dirs, files = parse_term_out(input_)
    state = {}
    walk_tree("/", fs["/"], 0, state)
    part1_answer = 0
    for k, v in state.items():
        if v <= 100000:
            part1_answer += v
    print(part1_answer)  # 1297683

    used_size = state["/"]
    disk_size = 70000000
    update_size = 30000000
    free_space = disk_size - used_size
    smallest_directory_larger_than = update_size - free_space
    print(
        min(
            [
                (dir, size)
                for dir, size in state.items()
                if smallest_directory_larger_than <= size
            ],
            key=lambda e: e[1],
        )
    )  # 5756764
