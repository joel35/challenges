import math


def round_to_next(number: int, multiple: int):
    round_down = math.floor(number / multiple) * multiple
    round_up = multiple if number % multiple else 0
    return round_down + round_up
