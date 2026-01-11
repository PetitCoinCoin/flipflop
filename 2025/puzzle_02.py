from functools import cache
from itertools import accumulate
from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def get_max_height(rc: str) -> int:
    def acc(x: int, y: str) -> int:
        if y == "^":
            return x + 1 
        return x - 1

    running_height = accumulate(rc, acc, initial = 0)
    return max(running_height)

def get_non_linear_max_height(rc: str) -> int:
    height = 0
    max_height = 0
    previous_char = ""
    delta = 0
    for char in rc:
        if char == previous_char:
            delta += 1
        else:
            delta = 1
        if char == "^":
            height += delta
        else:
            height -= delta
        max_height = max(height, max_height)
        previous_char = char
    return max_height

def get_fibo_max_height(rc: str) -> int:
    height = 0
    max_height = 0
    previous_char = ""
    counter = 0
    for char in rc:
        if char == previous_char:
            counter += 1
        else:
            if previous_char == "^":
                height += fib(counter)
            else:
                height -= fib(counter)
            counter = 1
        max_height = max(height, max_height)
        previous_char = char
    return max_height

@cache
def fib(n: int) -> int:
    if not n:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = file.read().strip()
    if args.part == 1:
        print(get_max_height(data))
    elif args.part == 2:
        print(get_non_linear_max_height(data))
    else:
        print(get_fibo_max_height(data))
    print(time() - t)
