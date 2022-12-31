from year2022.util import get_input


def main(input_):

    instructions = parse_input(input_)
    samples, crt = machine_run(instructions)
    return sum(samples), crt  # 15360, [[...],...]


def parse_input(input_: str):
    instructions = []
    for line in input_.splitlines():
        instruction, *args = line.split()
        args = [int(arg) for arg in args]
        instructions.append((instruction, args))
    return instructions


def machine_run(program: list) -> int:
    cycle = 0
    busy = 0
    registers = {"x": 1}
    crt = [["@" for _ in range(40)] for _ in range(6)]

    samples = []
    while True:
        cycle += 1

        # CPU
        if not busy:

            try:
                instruction = program.pop(0)

            except IndexError:
                break

            else:
                busy = cpu_cost_lookup[instruction[0]]

        # CRT
        h_pos = (cycle - 1) % 40
        v_pos = (cycle - 1) // 40
        pixel = "#" if registers["x"] - 1 <= h_pos <= registers["x"] + 1 else "."
        crt[v_pos][h_pos] = pixel

        signal_strength = cycle * registers["x"]
        if (cycle - 20) % 40 == 0:
            samples.append(signal_strength)

        # End of Cycle
        busy -= 1
        if not busy and instruction:
            process_instruction(instruction, registers)

    return samples, crt


def process_instruction(instruction, registers):
    if instruction[0] == "noop":
        return

    if instruction[0] == "addx":
        registers["x"] += instruction[1][0]


cpu_cost_lookup = {"noop": 1, "addx": 2}

example_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

if __name__ == "__main__":

    input_ = get_input(__file__)
    part1, crt = main(input_)
    print(f"{part1=}")
    for line in crt:
        print("".join(line))
    # PHLHJGZA
