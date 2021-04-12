def is_armstrong(n: int) -> bool:
    digits = [int(digit) for digit in str(n)]
    number = 0
    for digit in digits:
        number += digit ** len(digits)

    return True if number == n else False
