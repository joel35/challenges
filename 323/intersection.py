from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    common = set()

    for iterable in args:
        if not iterable:
            continue

        common = common.intersection(iterable) or set(iterable)

    return common
