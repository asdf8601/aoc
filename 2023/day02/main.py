"""
Advent of Code 2023
Day 2: part 1
"""
import sys
from pathlib import Path



def read_input() -> list[str]:
    fname = sys.argv[1]
    return Path(fname).read_text().strip().splitlines()


def get_cubes(subset: str, out: dict):
    cube_list = subset.replace(" cubes", "").replace(" and", "").split(", ")
    for _, cube in enumerate(cube_list):
        qty, color = cube.split(" ")
        qty = int(qty)
        if out.get(color, 0) < qty:
            out[color] =  qty


def get_max_cubes(line: str):
    subset_list = line.split(": ")[1].split("; ")
    out = {}
    for subset in subset_list:
        subset = subset.split(", ")
        for _, cube in enumerate(subset):
            qty, color = cube.split(" ")
            qty = int(qty)
            if out.get(color, 0) < qty:
                out[color] =  qty
    return out


def is_possible(used_cubes, available_cubes):
    for color, qty in used_cubes.items():
        if available_cubes.get(color, 0) < qty:
            return False
    return True


def get_game_id(line: str):
    game_id = int(line.split(":")[0].split(" ")[1].strip())
    return game_id


def test_game():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    cntrn = "12 red cubes, 13 green cubes, and 14 blue cubes"

    # get cubes
    available_cubes = {}
    get_cubes(cntrn, available_cubes)
    expected = {"red": 12, "green": 13, "blue": 14}
    assert available_cubes == expected
    print("test_game::get_cubes passed")

    # get id
    game_id = get_game_id(line)
    assert game_id == 1
    print("test_game::get_id passed")

    # get used cubes
    max_used_cubes = get_max_cubes(line)
    expected = {"red": 4, "blue": 6, "green": 2}
    assert max_used_cubes == expected
    print("test_game::get_used_cubes passed")

    # is possible
    assert is_possible(max_used_cubes, available_cubes) is True
    print("test_game::is_possible passed")


def prob1():
    cntrn = "12 red cubes, 13 green cubes, and 14 blue cubes"
    available_cubes = {}
    get_cubes(cntrn, available_cubes)

    lines = read_input()
    print(*lines, sep="\n")
    print(cntrn)

    total = 0
    for line in lines:
        game_id = line.split(":")[0].split(" ")[1].strip()
        used_cubes = get_max_cubes(line)
        is_posible = is_possible(used_cubes, available_cubes)
        print(f"game {game_id} is possible: {is_posible}")
        if is_posible:
            game_id = get_game_id(line)
            total += game_id

    print(f"{total = }")


def get_min_cubes(line: str):
    subset_list = line.split(": ")[1].split("; ")
    out = {}
    for subset in subset_list:
        subset = subset.split(", ")
        for _, cube in enumerate(subset):
            qty, color = cube.split(" ")
            qty = int(qty)
            if out.get(color, float("inf")) > qty:
                out[color] =  qty
    return out


def multiply(used_cubes: dict):
    out = None
    values = used_cubes.values()
    for v in values:
        if out is None:
            out = v
        else:
            out *= v
    return out


def prob2():

    lines = read_input()
    print(*lines, sep="\n")

    total = 0
    for line in lines:
        game_id = line.split(":")[0].split(" ")[1].strip()
        used_cubes = get_max_cubes(line)
        power = multiply(used_cubes)
        total += power
        print(f"game {game_id} | mininum cubes: {used_cubes} | power: {power} | total: {total}")

    print(f"{total = }")



def main():
    prob2()

if __name__ == "__main__":
    main()
