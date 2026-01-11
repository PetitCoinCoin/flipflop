from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def distance(a: tuple[int], b: tuple[int], *, with_diagonal: bool) -> int:
    xa, ya = a
    xb, yb = b
    dx = abs(xa - xb)
    dy = abs(ya - yb)
    if with_diagonal:
        return max(dx, dy)
    return dx + dy

def pick_in_order(*, with_diagonal: bool) -> int:
    start = (0, 0)
    steps = 0
    for trash in data:
        steps += distance(start, trash, with_diagonal=with_diagonal)
        start = trash
    return steps

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = [tuple(int(x) for x in line.split(",")) for line in file.read().strip().split("\n")]
    if args.part == 1:
        print(pick_in_order(with_diagonal=False))
    elif args.part == 2:
        print(pick_in_order(with_diagonal=True))
    else:
        data.sort(key=lambda x: distance((0, 0), x, with_diagonal=False))
        print(pick_in_order(with_diagonal=True))
    print(time() - t)
