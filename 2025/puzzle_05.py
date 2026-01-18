from pathlib import Path
from time import time

from py_utils.parsers import parse_args

def get_steps(pos: int = 0, *, powered: bool) -> int:
    tunnel = data[pos]
    seen.add(tunnel)
    end = next(p for p in transitions[tunnel] if p != pos)
    if end == len(data) - 1:
        return pos - end if powered and tunnel.isupper() else end - pos
    steps = -abs(end - pos) if powered and tunnel.isupper() else abs(end - pos)
    return steps + get_steps(end + 1, powered=powered)

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = file.read().strip()
    transitions = dict()
    for i, char in enumerate(data):
        transitions[char] = transitions.get(char, []) + [i]
    seen = set()
    steps = get_steps(powered=args.part == 3)
    if args.part != 2:
        print(steps)
    elif args.part == 2:
        unseen = ""
        for tunnel in data:
            if tunnel not in seen and tunnel not in unseen:
                unseen += tunnel
        print(unseen)
    print(time() - t)
