import pytest
from year2022.day_01.__main__ import main, get_input


def test_example_main(example_input):
    part_1_answer, part_2_answer = main(example_input)
    assert part_1_answer == 24000
    assert part_2_answer == 45000


def test_main(_input):
    part_1_answer, part_2_answer = main(_input)
    assert part_1_answer == 66719
    assert part_2_answer == 198551


@pytest.fixture
def example_input():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


@pytest.fixture
def _input():

    return get_input()
