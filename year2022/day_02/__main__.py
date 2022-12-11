from year2022.util import get_input

player1_symbol = {"A": "r", "B": "p", "C": "s"}
player2_symbol = {"X": "r", "Y": "p", "Z": "s"}
winning_moves = (("r", "s"), ("p", "r"), ("s", "p"))
move_score = {"r": 1, "p": 2, "s": 3}

move_twister = {
    ("A", "X"): "C",
    ("A", "Y"): "A",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Y"): "B",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Y"): "C",
    ("C", "Z"): "A",
}


def compute_score(data):
    player1_score = 0
    for move in data:
        player1_score += score_round(move)[1] + move_score[move[1]]

    return player1_score


def decode_move(move):

    decoded = (move[0], move_twister[move])

    return decoded


def score_round(move):

    if move[0] == move[1]:
        return (3, 3)

    if move in winning_moves:
        return (6, 0)

    return (0, 6)


if __name__ == "__main__":
    data = []
    for line in get_input(__file__).splitlines():
        pair = line.split()

        data.append((player1_symbol[pair[0]], player2_symbol[pair[1]]))

    print(compute_score(data))

    data = []
    for line in get_input(__file__).splitlines():
        pair = tuple(line.split())

        move = decode_move(pair)
        data.append((player1_symbol[move[0]], player1_symbol[move[1]]))

    print(compute_score(data))
