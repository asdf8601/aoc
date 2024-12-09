#!/usr/bin/env python3.13

def read_input(fname: str):
    with open(fname, 'r') as f:
        for line in map(str.strip, f):
            yield line


def parse_mul(line):
    import re
    m = re.finditer(r'mul(\(\d{1,3},\d{1,3}\))', line)
    total = 0

    for i in m:
        a, b = map(int, i.group(1)[1:-1].split(','))
        total += a*b

    return total

def part1(lines):
    total = 0
    for line in lines:
        print(line)
        out = parse_mul(line)
        total += out
    print(total)


def part2(lines):
    import re

    grand_total = 0
    for line in lines:
        # line = "don't()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))do()"
        # ops = re.sub(r"don't\(\).*?mul(\(\d{1,3},\d{1,3}\))", "", line)
        ops = line
        ops = re.sub(r"don't\(\).*?do\(\)", "", ops)
        ops = re.sub(r"don't\(\).*?do", "", ops)
        ops = re.sub(r"n't\(\).*?do\(\)", "", ops)
        ops = re.sub(r"don't\(\).*", "", ops)

        if "don't" in ops:
            return ops
        iter = re.finditer(r'mul(\(\d{1,3},\d{1,3}\))', ops)
        total = 0
        for it in iter:
            a, b = map(int, it.group(1)[1:-1].split(','))
            total += a*b
        grand_total += total

    return grand_total


if __name__ == "__main__":
    # lines = read_input("./part1.test.txt")
    # lines = read_input("./part1.txt")
    # part1(lines)
    # lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    # lines = read_input("./part2.test.txt")
    lines = read_input("./part1.txt")
    print(part2(lines))
