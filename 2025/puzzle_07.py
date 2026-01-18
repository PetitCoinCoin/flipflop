from functools import cache
from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def parse_input(line: str) -> tuple:
    return tuple(int(x) for x in line.split())

@cache
def get_nb_of_shortest_paths(grid: tuple[int]) -> int:
    x = min(grid)
    y = max(grid)
    if x == 2:
        return y
    return get_nb_of_shortest_paths((x - 1, y)) + get_nb_of_shortest_paths((x, y - 1))

@cache
def get_nb_of_shortest_paths_3d(grid: tuple[int]) -> int:
    x, y, z = grid
    if x < 2 or y < 2 or z < 2:
        reduced = (y, z) if x < 2 else ((x, z) if y < 2 else (x, y))
        return get_nb_of_shortest_paths(reduced)
    if x == 2 and (y == 2 or z == 2):
        return max(y, z) * (max(y, z) + 1)
    tot = sum(
        get_nb_of_shortest_paths_3d(new_grid)
        for new_grid in ((x - 1, y, z), (x, y - 1, z), (x, y, z - 1))
    )
    return tot

@cache
def get_nb_of_shortest_paths_any(grid: tuple[int], dimension: int) -> int:
    if dimension == 2:
        return get_nb_of_shortest_paths(grid)
    if any(n < 2 for n in grid):
        return get_nb_of_shortest_paths_any(tuple(n for n in grid if n >= 2), dimension - 1)
    tot = sum(
        get_nb_of_shortest_paths_any(tuple(grid[j] - 1 if j == i else grid[j] for j in range(dimension)), dimension)
        for i in range(dimension)
    )
    return tot

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = [parse_input(line) for line in file.read().strip().split("\n")]
    if args.part == 1:
        print(sum(get_nb_of_shortest_paths(g) for g in data))
    elif args.part == 2:
        print(sum(get_nb_of_shortest_paths_any((g[0], g[1], g[0]), 3) for g in data))
    else:
        print(sum(get_nb_of_shortest_paths_any((g[1],) * g[0], g[0]) for g in data))
    print(time() - t)
