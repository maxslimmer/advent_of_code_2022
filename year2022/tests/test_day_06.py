import pytest
from year2022.day_06.__main__ import part1, part2


def test_part1(input_):

    assert part1(input_) == 10


def test_part2():

    assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19


@pytest.fixture
def input_():

    return "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    return "nppdvjthqldpwncqszvftbrmjlhg"
    return "bvwbjplbgvbhsrlpgdmjqwftvncz"
