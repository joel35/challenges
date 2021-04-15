from typing import List


def minimum_number(digits: List[int]) -> int:
    return int(''.join(map(str, sorted(set(digits))))) if digits else 0
