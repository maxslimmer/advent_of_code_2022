import pytest
from year2022.day_05.__main__ import parse_input, get_input, part1, part2, build_move


def test_build_move():
    move_line = "move 3 from 1 to 2"
    expected = {"count": 3, "from": 1, "to": 2}
    move = build_move(move_line)

    assert expected == build_move(move_line)


def test_example_parse_input(_input):
    stacks, moves = parse_input(_input)
    assert stacks[3] == ["P"]
    assert moves[1] == {"count": 3, "from": 1, "to": 3}


def test_part1(_input):

    assert "CMZ" == part1(_input)


def test_part2(_input):

    assert "MCD" == part2(_input)


@pytest.fixture
def _input():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    return get_input()
