def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if type(value) not in [int, float]:
        raise TypeError
    if fmt not in ['cm', 'in']:
        raise ValueError
    return round(value*2.54 if fmt == 'cm' else value/2.54, 4)

