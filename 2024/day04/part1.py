#!/usr/bin/env python3.13
"""
Advent of code: DAY-4
---------------------
"""
import sys

def read_input(fname: str):
    with open(fname, 'r') as f:
        for line in map(str.strip, f):
            yield line

if len(sys.argv) != 2:
    DEBUG = False
else:
    DEBUG = sys.argv[1] == "debug"

def debug(*args):
    if DEBUG:
        print(*args)


def find_pattern(pattern, direction, lines):
    debug("direction:", direction)
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
                rowi = row+(row_dir*step)
                coli = col+(col_dir*step)
                text += lines[rowi][coli]
            if find:= text == pattern:
                total += 1
                debug(row, col, text, find, direction)


    return total

def print_matrix(lines, Y):
    debug("  "+"".join(map(str, range(Y))))
    for i, line in enumerate(lines):
        debug(i, line)
    debug()

def part1(lines):
    lines = list(lines)
    Y = len(lines[0])

    print_matrix(lines, Y)

    grand_total = 0
    patterns = ["XMAS"]
    directions = [(0,-1),(-1,0),(0,1), (1,0), (1,1), (1,-1), (-1, 1), (-1, -1)]
    for direction in directions:
        for pattern in patterns:
            if total:=find_pattern(pattern, direction, lines):
                grand_total += total

    print("Total patterns found: ", grand_total)



if __name__ == "__main__":
    lines = read_input("./part1.test.txt")
    # lines = read_input("./part1.txt")
    part1(lines)

