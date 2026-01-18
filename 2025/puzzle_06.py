from pathlib import Path
from time import time

from py_utils.parsers import parse_args

SKY = 1000
FRAME = range(250, 750)

def parse_input(line: str) -> tuple:
    return tuple(int(x) for x in line.split(","))

def get_position_at(bird: tuple[int], sec: int) -> tuple[int]:
    vx, vy = bird
    return ((vx * sec) % SKY, (vy * sec) % SKY)

def is_in_frame_at(bird: tuple[int], sec: int) -> bool:
    x, y = get_position_at(bird, sec)
    return x in FRAME and y in FRAME

if __name__ == "__main__":
    args = parse_args()
    t = time()
    with Path(f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = [parse_input(line) for line in file.read().strip().split("\n")]
    if args.part == 1:
        print(sum(is_in_frame_at(b, 100) for b in data))
    else:
        delta_sec = 3600 if args.part == 2 else 31556926
        print(
            sum(
                sum(is_in_frame_at(b, sec) for b in data)
                for sec in range(delta_sec, delta_sec * 1000 + 1, delta_sec)
                )
        )
    print(time() - t)
