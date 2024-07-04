from dataclasses import dataclass


@dataclass
class Region:
    start_x: float
    start_y: float
    amount_x: int
    amount_y: int
    step: int
    list_op_points: list


def create_region(start_x, start_y, amount_x, amount_y, step):
    return Region(start_x,
                  start_y,
                  int(amount_x / step),
                  int(amount_y / step),
                  step,
                  [(x * step + start_x, y * step + start_y) for x in range(int(amount_x / step)) for y in
                   range(int(amount_y / step))])
