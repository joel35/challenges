def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""

    return len([i for i in my_cities + other_cities if i not in my_cities or i not in other_cities])
