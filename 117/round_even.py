def round_even(number):
    """Takes a number and returns it rounded even"""
    rounded = int(round(number, 0))
    return rounded+1 if number % .5 == 0 and rounded % 2 != 0 else rounded

