import math
from year2022.util import get_input


def parse_input(input_: str) -> tuple[str, int]:
    moves = []
    for line in input_.splitlines():
        move = line.split()
        direction, distance = move[0], int(move[1])
        moves.append((direction, distance))

    return moves


def main(input_):
    moves = parse_input(input_)
    tail_pos = head_pos = (0, 0)
    tail_visits = set((tail_pos,))

    for direction, steps in moves:
        for _ in range(steps):
            head_pos, tail_pos = execute_move(direction, *head_pos, *tail_pos)
            tail_visits.add(tail_pos)

    return len(tail_visits)


VECTORS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def reduce_to_one(c):
    if not c:
        return c

    return c // abs(c)


def execute_move(move, head_x, head_y, tail_x, tail_y):

    # lead with the head
    vx, vy = VECTORS[move]
    head_pos = (head_x + vx, head_y + vy)

    # the tail follows
    vector, distance = get_offset(*head_pos, tail_x, tail_y)
    if distance <= math.sqrt(2):
        return head_pos, (tail_x, tail_y)

    tail_pos = tail_x + reduce_to_one(vector[0]), tail_y + reduce_to_one(vector[1])

    return head_pos, tail_pos


def get_offset(x0, y0, x1, y1):

    distance = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    vector = (x0 - x1), (y0 - y1)
    return vector, distance


if __name__ == "__main__":

    input_ = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    input_ = get_input(__file__)

    print(main(input_))  # 6311
