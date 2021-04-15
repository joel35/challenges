from typing import List


def minimum_number(digits: List[int]) -> int:
    deduped = set([d for d in digits if d])
    return int(''.join(map(str, sorted(deduped)))) if deduped else 0
