from collections import Counter


def freq_digit(num: int) -> int:
    n = [int(i) for i in str(num)]
    return Counter(n).most_common()[0][0]
