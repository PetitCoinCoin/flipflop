from collections import Counter
from itertools import pairwise
from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def score_name(banana: str, *, with_substitue: bool = True) -> int:
    pairs = pairwise(banana)
    count = Counter(("".join(p) for p in pairs))
    if not with_substitue and count["ne"]:
        return 0
    return count["ba"] + count["na"] + count["ne"]

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = file.read().strip().split("\n")
    if args.part == 1:
        print(sum(score_name(b) for b in data))
    elif args.part == 2:
        print(sum(score for b in data if not (score:=score_name(b)) % 2))
    else:
        print(sum(score_name(b, with_substitue=False) for b in data))
    print(time() - t)
