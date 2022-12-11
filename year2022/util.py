from pathlib import Path


def get_input(basedir):

    with Path(basedir).parent.joinpath("input.txt").open("r") as input_file:
        input_ = input_file.read()

    return input_
