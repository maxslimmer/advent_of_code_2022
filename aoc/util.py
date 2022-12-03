from pathlib import Path


def get_data(basedir):

    with Path(basedir).parent.joinpath("data.txt").open("r") as data_file:
        data = data_file.read()

    return data
