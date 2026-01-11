from collections import Counter
from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def get_label(bush: str) -> str:
    r, g, b = map(int, bush.split(","))
    if r == g or r == b or b == g:
        return "S"
    if r > g and r > b:
        return "R"
    if b > r and b > g:
        return "B"
    return "G"

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = file.read().strip().split("\n")
    if args.part == 1:
        print(Counter(data).most_common(1)[0][0])
    elif args.part == 2:
        print(sum(1 for b in data if get_label(b) == "G"))
    else:
        PRICE_MAP = {"R": 5, "G": 2, "B": 4, "S": 10}
        print(sum(PRICE_MAP[get_label(b)] for b in data))
    print(time() - t)
