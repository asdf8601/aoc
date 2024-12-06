# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///
import logging
from typing import Generator


def read_file(file_path:str) -> Generator[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield map(int, line.strip().split())


def is_safe(report:str) -> bool:
    levels = map(int, report.split())
    a = next(levels)
    b = next(levels)
    diff = b-a
    if diff == 0:
        return False
    elif abs(diff) > 3:
        return False
    dir_a = diff/abs(diff)
    a = b
    for b in levels:
        diff = b-a
        if diff == 0:
            return False
        dir = diff/abs(diff)
        if abs(diff) > 3 or dir != dir_a:
            return False
        a = b
        dir_a = dir
    return True


def part1(fname:str):
    lines = read_file(fname)
    total = 0
    for line in lines:
        if is_safe(line):
            total += 1
    print("total:", total)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    # part1('part1-test.txt')
    part1('part1.txt')
