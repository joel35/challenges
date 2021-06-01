from typing import List, TypeVar

T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    new_list = []

    for number in numbers:
        # append number to list if zero
        if number == 0:
            new_list.append(number)
            continue

        # convert float into int
        if type(number) is float:
            number = convert_float(number)

        # fix number length
        while number_length(number) != n:
            number = int(number / 10) if number_length(number) > n else number * 10

        new_list.append(number)

    return new_list


def number_length(n):
    return len(str(n).strip('-'))


def convert_float(n):
    dp = len(str(n).split('.')[1])
    for _ in range(dp):
        n = n * 10
    return int(round(n))
