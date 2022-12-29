import math
from year2022.util import get_input


def parse_input(input_: str) -> tuple[str, int]:
    moves = []
    for line in input_.splitlines():
        move = line.split()
        direction, distance = move[0], int(move[1])
        moves.append((direction, distance))

    return moves


KNOT_COUNT = 10


def main(input_):
    moves = parse_input(input_)
    rope = [(0, 0) for _ in range(KNOT_COUNT)]
    tail_visits = set((rope[-1],))

    for direction, steps in moves:
        for _ in range(steps):
            rope = execute_move(direction, rope)
            tail_visits.add(rope[-1])

    return len(tail_visits)


VECTORS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def reduce_to_one(c):
    if not c:
        return c

    return c // abs(c)


def execute_move(move, rope: list):
    new_rope = rope.copy()

    # lead with the head
    vx, vy = VECTORS[move]
    new_rope[0] = (rope[0][0] + vx, rope[0][1] + vy)

    # the followers react
    leader = new_rope[0]
    for follower_number, follower in enumerate(new_rope[1:], 1):
        fx, fy = follower
        vector, distance = get_offset(*leader, fx, fy)
        if distance <= math.sqrt(2):
            # no movement required
            break
        leader = fx + reduce_to_one(vector[0]), fy + reduce_to_one(vector[1])

        new_rope[follower_number] = leader

    return new_rope


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
