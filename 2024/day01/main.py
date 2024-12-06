def read_file(file_path):
    with open(file_path, 'r') as f:
        yield from f


def part1(fname):
    col1 = []
    col2 = []
    for line in read_file(fname):
        _a, _b = line.split()
        a = int(_a)
        b = int(_b)
        col1.append(a)
        col2.append(b)

    sorted_col1 = sorted(col1)
    sorted_col2 = sorted(col2)

    total = 0
    for i in range(len(col1)):
        dist = abs(sorted_col1[i] - sorted_col2[i])
        total += dist

    print(total)


def part2(fname):
    col1 = []
    col2 = []
    for line in read_file(fname):
        _a, _b = line.split()
        a = int(_a)
        b = int(_b)
        col1.append(a)
        col2.append(b)

    similar = []
    for num in col1:
        similarity = 0
        for num2 in col2:
            if num == num2:
                similarity += 1
        similar.append(num * similarity)
    # print(similar)
    print(sum(similar))


if __name__ == '__main__':
    # part1(fname="./part1-test.txt")
    # part1(fname="./part1.txt")
    part2(fname="./part1-test.txt")
    part2(fname="./part1.txt")
