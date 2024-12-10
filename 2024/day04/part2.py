#!/usr/bin/env python3.13
"""
Advent of code: DAY-4
---------------------
"""

def read_input(fname: str):
    with open(fname, 'r') as f:
        for line in map(str.strip, f):
            yield line


def debug(*args):
    print(*args)


def find_pattern(pattern, direction, lines, show=False):
    pattern_len = len(pattern)
    row_len = len(lines)
    col_len = len(lines[0])
    offset = pattern_len - 1

    col_start = 0
    col_end = col_len

    row_start = 0
    row_end = row_len

    row_dir, col_dir = direction

    if row_dir == 1:
        row_start = 0
        row_end = row_len - offset
    elif row_dir == -1:
        row_start = offset
        row_end = row_len

    if col_dir == 1:
        col_start = 0
        col_end = col_len - offset
    elif col_dir == -1:
        col_start = offset
        col_end = col_len

    total = 0
    find = False
    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            text = ""
            for step in range(pattern_len):
                rowi = row + (row_dir * step)
                coli = col + (col_dir * step)
                text += lines[rowi][coli]
            if find := text == pattern:
                total += 1
                if show:
                    debug(row, col, text, find, direction)

    return total


def print_matrix(lines):
    col_size = len(lines[0])
    debug("  " + "".join(map(str, range(col_size))))
    for i, line in enumerate(lines):
        debug(i, line)
    debug()


def build_x_line(lines: list[list[str]]):
    for i in range(0, len(lines)-2):
        for j in range(0, len(lines[i])-2):
            yield [row[j:j+3] for row in lines[i:i+3]]


def part2(raw_lines):
    raw_lines = list(raw_lines)
    # print_matrix(raw_lines)

    total = 0
    pattern = "MAS"
    directions = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    for lines in build_x_line(raw_lines):
        findings = 0
        for direction in directions:
            if find := find_pattern(pattern, direction, lines, False):
                findings += find
        if findings >= 2:
            # print_matrix(lines)
            total += 1
    print("Total patterns found: ", total)


if __name__ == "__main__":
    lines = read_input("./part1.test.txt")
    # lines = read_input("./part1.txt")
    part2(lines)
