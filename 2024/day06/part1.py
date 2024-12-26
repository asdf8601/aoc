#!/usr/bin/env python3.13
"""
Advent of code: DAY-6
---------------------
"""
# HACK: modify maxrecursion tolerance so we can explore the whole matrix
import sys
sys.setrecursionlimit(1_000_000)

def read_input(fname: str) -> list[list[str]]:
    with open(fname, 'r') as f:
        return [list(line.lower()) for line in map(str.strip, f)]


def find_guard(lines) -> tuple[str, int, int]:
    guard = ["^", "v", "<", ">"]
    for row_idx, row in enumerate(lines):
        for g in guard:
            if g in row:
                return g, row_idx, row.index(g)


def guard_walk(guard, lines: list[list[str]]):
    # origin
    dir = guard[0]
    row = guard[1]
    col = guard[2]

    # one step
    if dir == "^":
        drow = -1
        dcol = 0
    elif dir == "v":
        drow = 1
        dcol = 0
    elif dir == "<":
        drow = 0
        dcol = -1
    elif dir == ">":
        drow = 0
        dcol = 1
    else:
        drow = 0
        dcol = 0

    next_col = col + dcol
    next_row = row + drow

    # out of bounds
    if (
        (next_row < 0 or next_row >= len(lines)) or
        (next_col < 0 or next_col >= len(lines[0]))
    ):
        dir = "x"
        lines[row][col] = "x"
        return dir, row, col

    # no-block
    if lines[next_row][next_col] != "#":
        lines[row][col] = 'x'
        lines[next_row][next_col] = dir

    # block
    elif lines[next_row][next_col] == "#":
        if dir in "^":
            dir = ">"
        elif dir in "v":
            dir = "<"
        elif dir in "<":
            dir = "^"
        elif dir in ">":
            dir = "v"

        lines[row][col] = dir
        next_row = row
        next_col = col

    print_step(guard, lines)

    return guard_walk((dir, next_row, next_col), lines)


def part1(lines: list[list[str]]):
    lines = list(lines)
    guard = find_guard(lines)
    print_step(guard, lines)
    try:
        guard = guard_walk(guard, lines)
    except RecursionError:
        print_step(guard, lines, True)

    print_step(guard, lines)
    total = sum(map(lambda x: x=="x", "".join(map("".join, lines))))
    print()
    print(f"{total = }")


def print_step(guard, lines, matrix=False):
    print()
    print(f'{guard = }')
    if matrix:
        print_matrix(lines)

def print_matrix(lines):
    print("    ", *map(lambda x: "{:< 4d}".format(x), range(len(lines))), sep="")
    for i, line in enumerate(lines):
        print("{:> 4d} ".format(i), *map(lambda x: f"{x}   ", line), sep="")



if __name__ == "__main__":
    # lines = read_input("./part1.test.txt")
    lines = read_input("./part1.txt")
    part1(lines)
