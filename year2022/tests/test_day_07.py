import pytest

from year2022.day_07.__main__ import parse_term_out


def test_file_system(input_):

    fs, dirs, files = parse_term_out(input_)
    assert fs["/"]["a"]["e"]["i"] == 584


@pytest.fixture
def input_():

    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
