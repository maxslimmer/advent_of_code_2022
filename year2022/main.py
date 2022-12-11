from pathlib import Path
import sys

import requests

SESSION = "53616c7465645f5fa35c0011679efbe69691509c805243824a5c4ac018a3a348f9f3e27832374580513a6975211a1624eeb35df264d8ffd874074f39a4b7d85b"

session = requests.Session()
session.cookies.set("session", SESSION)


def create_new_day(day_number):

    day_dir = Path(_format_day_dir(day_number))

    day_dir.mkdir(exist_ok=True)
    day_dir.joinpath("__init__.py").touch(exist_ok=True)
    day_dir.joinpath("__main__.py").touch(exist_ok=True)


def fetch_data(day_number):

    data_url = f"https://adventofcode.com/2022/day/{day_number}/input"
    day_dir = Path(_format_day_dir(day_number)).joinpath("input.txt")
    resp = session.get(data_url)

    with day_dir.open("w", encoding="utf8") as data_file:
        data_file.write(resp.text)


def _format_day_dir(day_number):
    return f"day_{day_number:02}"


def main():

    day = int(sys.argv[1])

    create_new_day(day_number=day)
    fetch_data(day)


if __name__ == "__main__":
    main()
