#!/usr/bin/env python3.13
"""
Advent of code: DAY-5
---------------------
"""
from typing import Generator


def read_input(fname: str):
    with open(fname, 'r') as f:
        for line in map(str.strip, f):
            yield line


def debug(*args):
    print(*args)


def part1(lines: list[str]|Generator[str]):

    sorting_rules = []
    update_pages = []

    for line in lines:

        if "|" in line:
            # debug(line)
            a, b = map(int, line.split("|"))
            sorting_rules.append((a,b))

        elif "," in line:
            # debug(line)
            update_pages.append(list(map(int, line.split(","))))


    update_ok_list = []
    middle_list = []

    for page in update_pages:
        if len(page) % 2 == 0:
            print("Warning: middle is even")
        # print(f"=== {page=}")
        is_ok = True

        for (a,b) in sorting_rules:
            # print(f"{a=}, {b=}")

            if a not in page or b not in page:
                continue

            a_idx = page.index(a)
            b_idx = page.index(b)
            # print(f"{a_idx=}, {b_idx=}")

            if a_idx > b_idx:
                is_ok = False
                continue

        if is_ok:
            update_ok_list.append(page)
            middle_idx = len(page) // 2
            middle = page[middle_idx]
            # print(f"{middle=} {middle_idx=}")
            middle_list.append(middle)

    print(f"{middle_list=}")
    print(f"{sum(middle_list)=}")


if __name__ == "__main__":
    # lines = read_input("./part1.test.txt")
    lines = read_input("./part1.txt")
    part1(lines)
