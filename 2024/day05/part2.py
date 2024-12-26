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


def check_rules(page: list[int], rules: list[tuple[int, int]], iter=0) -> bool:
    for (a,b) in rules:

        if a not in page or b not in page:
            continue

        a_idx = page.index(a)
        b_idx = page.index(b)

        if a_idx > b_idx:
            page[a_idx], page[b_idx] = page[b_idx], page[a_idx]
            return check_rules(page, rules, iter+1)
    if iter == 0:
        return False
    return True


def part2(lines: list[str]|Generator[str]):

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

        if check_rules(page, sorting_rules):
            update_ok_list.append(page)
            middle_idx = len(page) // 2
            middle = page[middle_idx]
            middle_list.append(middle)

    print(f"{middle_list=}")
    print(f"{sum(middle_list)=}")


if __name__ == "__main__":
    # lines = read_input("./part1.test.txt")
    lines = read_input("./part1.txt")
    part2(lines)
