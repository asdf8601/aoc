#!/usr/bin/env python3.13
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pillow",
# ]
# ///
"""
Advent of code: DAY-6
---------------------

convert -delay 100 step_*.png animation.gif
convert -delay 10 step_*.png animation.gif
"""
# HACK: modify maxrecursion tolerance so we can explore the whole matrix
import sys
import os

sys.setrecursionlimit(1_000_000)

PRINT_COUNTER = 0
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
BLOCK = "#"
BLOCK_VIRTUAL = "O"
NODIR = "X"

DIRECTIONS = ("^", "v", "<", ">")

VISITED = {
    "^": "|",
    "v": "|",
    "<": "-",
    ">": "-",
}

TURN_RIGHT = {
    "^": ">",
    "v": "<",
    "<": "^",
    ">": "v",
}

STEP = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def read_input(fname: str) -> list[list[str]]:
    with open(fname, "r") as f:
        return [list(line.lower()) for line in map(str.strip, f)]


def find_guard(lines) -> tuple[str, int, int]:
    for row_idx, row in enumerate(lines):
        for g in DIRECTIONS:
            if g in row:
                return g, row_idx, row.index(g)
    raise ValueError("Guard not found")


def move(
    guard,
    lines,
    corners,
    blockers=[BLOCK],
):
    # origin
    dir = guard[0]
    row = guard[1]
    col = guard[2]

    # one step
    drow, dcol = STEP[dir]
    next_col = col + dcol
    next_row = row + drow

    visited = VISITED[dir]

    if (next_row < 0 or next_row >= len(lines)) or (
        next_col < 0 or next_col >= len(lines[0])
    ):
        # out of bounds
        dir = NODIR
        lines[row][col] = visited
        return dir, row, col

    elif lines[next_row][next_col] in blockers:
        # block
        dir = TURN_RIGHT[dir]
        corners.append((row, col))
        lines[row][col] = dir
        next_row = row
        next_col = col
    else:
        # non-block
        lines[row][col] = visited
        lines[next_row][next_col] = dir

    return dir, next_row, next_col


def guard_walk(
    guard_status,
    lines: list[list[str]],
    corners: list[tuple[int, int]],
    blocks=[BLOCK],
):
    loop_count = 0
    path = []
    no_loop_visited = []
    loop_visited = []
    while guard_status[0] != NODIR:
        guard_status = move(guard_status, lines, corners, blocks)
        print_step(guard_status, lines, show_matrix=True)
        is_loop = check_loop(
            guard_status,
            [ln[:] for ln in lines],
            corners,
            no_loop_visited=no_loop_visited,
            loop_visited=loop_visited,
        )
        if is_loop:
            loop_count += 1
        path.append(guard_status)
    print(f"{loop_count = }")
    return


def add_virtual_blocker(guard_status, lines):
    dir, row, col = guard_status
    drow, dcol = STEP[dir]
    next_row = row + drow
    next_col = col + dcol

    if (next_row < 0 or next_row >= len(lines)) or (
        next_col < 0 or next_col >= len(lines[0])
    ):
        return False
    lines[next_row][next_col] = BLOCK_VIRTUAL
    return True


def check_loop(
    guard,
    lines,
    corners,
    no_loop_visited=[],
    loop_visited=[],
):
    """
    Check if the guard's path forms a loop.
    Returns (is_loop, loop_start_idx, loop_length) if a loop is found,
    otherwise returns (False, None, None)
    """
    blockers=[BLOCK, BLOCK_VIRTUAL]
    # Keep track of visited positions and when we visited them
    visited = []
    out = False

    if guard[0] == NODIR:
        no_loop_visited.append(visited)
        return False
    elif not add_virtual_blocker(guard, lines):
        no_loop_visited.append([guard])
        return False
    elif any(guard in v for v in no_loop_visited):
        return False
    # elif any(guard in v for v in loop_visited):
    #     return True

    while guard[0] != NODIR:

        if guard[0] == NODIR:
            no_loop_visited.append(visited)
            return False
        elif any(guard in v for v in no_loop_visited):
            return False
        elif guard in visited:
            loop_visited.append(visited)
            return True
        # elif any(guard in v for v in loop_visited):
        #     return True

        visited.append(guard)
        guard = move(guard, lines, corners, blockers)
        print_step(guard, lines, show_matrix=True, indent=8)
        # if DEBUG:
        #     breakpoint()

    return out


def part2(lines: list[list[str]]):
    lines = list(lines)

    guard_status = find_guard(lines)
    print_step(guard_status, lines)

    corners = []
    guard_status = guard_walk(guard_status, lines, corners)
    print_step(guard_status, lines, show_matrix=True)


def print_matrix(lines, indent=0):
    pad = " " * indent
    print(
        f"{pad}    ",
        *map(lambda x: "{:< 4d}".format(x), range(len(lines))),
        sep="",
    )
    for i, line in enumerate(lines):
        print(f"{pad}{i:> 4d} ", *map(lambda x: f"{x}   ", line), sep="")


def print_step(
    guard_status,
    lines,
    show_matrix=False,
    indent=0,
):
    global PRINT_COUNTER
    draw_matrix(guard_status, lines, f'step_{PRINT_COUNTER:04d}.png')
    PRINT_COUNTER += 1
    if not DEBUG:
        return
    print()
    pad = " " * indent
    print(f"{pad}{guard_status = }")
    if show_matrix:
        print_matrix(lines, indent)



def draw_matrix(guard, lines, filename='matrix.png', cell_size=50):
    """
    Draw the matrix as a PNG image with colored cells.

    Args:
        lines: The matrix to draw
        filename: Output filename
        cell_size: Size of each cell in pixels
    """
    from PIL import Image, ImageDraw, ImageFont
    text_margin = 40
    # Define colors for different elements
    colors = {
        '.': (255, 255, 255),  # Empty - White
        '#': (0, 0, 0),        # Block - Black
        'O': (128, 128, 128),  # Virtual Block - Gray
        '|': (0, 255, 0),      # Vertical path - Green
        '-': (0, 255, 0),      # Horizontal path - Green
        '^': (255, 0, 0),      # Guard up - Red
        'v': (255, 0, 0),      # Guard down - Red
        '<': (255, 0, 0),      # Guard left - Red
        '>': (255, 0, 0),      # Guard right - Red
    }
    height = len(lines) * cell_size + text_margin
    width = len(lines[0]) * cell_size

    # Create a new image with white background
    image = Image.new('RGB', (width, height), 'white')

    # Draw guard status at the top
    draw = ImageDraw.Draw(image)
    status_text = f"{guard=}"
    draw.text((10, 10), status_text, fill=(255, 255, 255), font=None, font_size=20)
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw each cell
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Get cell color
            cell = lines[row][col]
            color = colors.get(cell, (200, 200, 200))  # Default to light gray

            # Draw filled rectangle
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=(100, 100, 100))

            # Draw the character in the center of the cell
            if cell not in ['.', '#']:
                # Calculate text position
                font_size = cell_size // 2
                text_bbox = draw.textbbox((x1, y1), cell, font=None, font_size=font_size)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                text_x = x1 + (cell_size - text_width) // 2
                text_y = y1 + (cell_size - text_height) // 2

                # Draw text in black
                draw.text((text_x, text_y), cell, fill=(0, 0, 0), font=None, font_size=font_size)

    # Save the image
    image.save(filename)

if __name__ == "__main__":
    if DEBUG:
        test = ".test"
    else:
        test = ""
    lines = read_input(f"./part1{test}.txt")
    part2(lines)
