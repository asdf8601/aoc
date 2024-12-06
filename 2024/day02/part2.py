"""
The engineers are surprised by the low number of safe reports until they
realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety
systems tolerate a single bad level in what would otherwise be a safe report.
It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an
unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can
remove a single level from unsafe reports. How many reports are now safe?
"""


def has_valid_differences(sequence):
    """Check if differences between adjacent elements are less than 4."""
    for i in range(len(sequence) - 1):
        if abs(sequence[i] - sequence[i + 1]) >= 4:
            return False
    return True


def test_has_valid_differences():

    cases = (
        (1, [1 , 4  , 3] , True) ,
        (2, [3 , 0  , 3] , True) ,
        (3, [3 , -2 , 1] , False) ,
        (4, [3 , 0 , -1] , True) ,
        (7, [1, 2, 7, 8, 9], False),
    )

    assert_all(has_valid_differences, cases)


def is_increasing(sequence):
    """Check if a sequence is non-decreasing (each number >= previous)."""
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


def test_is_increasing():
    cases = (
        (1, [1 , 4  , 3] , False) ,
        (3, [3 , 4  , 5] , True) ,
        (2, [3 , 0  , 1] , False) ,
        (4, [5 , 4  , 3] , False) ,
        (5, [3 , 0  , 0] , False) ,
        (6, [0  , 0] , False) ,
        (7, [1, 2, 7, 8, 9], True),
    )
    assert_all(is_increasing, cases)


def is_decreasing(sequence):
    """Check if a sequence is non-increasing (each number <= previous)."""
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            return False
    return True


def test_is_decreasing():
    cases = (
        (1, [1 , 4  , 3] , False) ,
        (3, [3 , 4  , 5] , False) ,
        (2, [3 , 0  , 1] , False) ,
        (4, [5 , 4  , 3] , True) ,
        (5, [3 , 0  , 0] , False) ,
        (6, [0  , 0] , False) ,
        (7, [1, 2, 7, 8, 9], False),
    )
    assert_all(is_decreasing, cases)


def is_safe_report(report):
    """Check if a report is inherently safe (monotonic)."""
    return (is_increasing(report) or is_decreasing(report)) and has_valid_differences(report)


def test_is_safe_report():
    cases = (
        (1, [1 , 4  , 3] , False) ,
        (3, [3 , 4  , 5] , True) ,
        (2, [3 , 0  , 1] , False) ,
        (4, [5 , 4  , 3] , True) ,
        (5, [3 , 0  , 0] , False) ,
        (6, [0  , 0] , False) ,
        (7, [1, 2, 7, 8, 9], False),
    )
    assert_all(is_safe_report, cases)


def can_be_safe(report):
    """Check if removing one number can make the report safe."""
    if len(report) < 3:
        return False

    for i in range(len(report)):
        # Try removing each number one at a time
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            print(f"Report {report} can be made safe by removing {report[i]}")
            return modified_report
    return False


def test_can_be_safe():
    cases = (
        (1, [1 , 4  , 3] , [4 , 3]) ,
        (2, [3 , 0  , 1] , [0, 1]) ,
        (3, [3 , 4  , 5] , [4, 5]) ,
        (4, [5 , 4  , 3] , [4 , 3]) ,
        (5, [3 , 0  , 0] , [3, 0]) ,
        (6, [0 , 0]      , False) ,
        (7, [1, 2, 7, 8, 9], False),
    )
    assert_all(can_be_safe, cases)


def assert_all(f, cases):
    for i, case, expected in cases:
        obtained = f(case)
        assert obtained == expected, f"{i=}: {case=} {expected=} {obtained=}"


def process_reports(reports: list[int]):
    """Read and process reports from a file."""
    safe_count = 0
    i = 0
    for i, report in enumerate(reports, 1):
        inc = is_increasing(report)
        dec = is_decreasing(report)
        dif = has_valid_differences(report)
        if (inc or dec) and dif:
            is_safe = True
        elif can_be_safe(report):
            is_safe = True
        else:
            is_safe = False

        status = "SAFE" if is_safe else "UNSAFE"
        print(f"Report {i}: {report} - {status}")
        if is_safe:
            safe_count += 1

    print(f"\nTotal reports processed: {i}")
    print(f"Safe reports: {safe_count}")
    print(f"Unsafe reports: {i - safe_count}")


def read_file(file_path:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield list(map(int, line.strip().split()))

if __name__ == "__main__":
    # reports = read_file("./part1-test.txt")
    # reports = read_file("./part1-test.txt")
    reports = read_file("./part1.txt")
    process_reports(reports=reports)
