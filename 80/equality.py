from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""

    if list1 is list2:
        n = 4
    elif list1 == list2:
        n = 3
    elif sorted(list1) == sorted(list2):
        n = 2
    elif set(list1) == set(list2):
        n = 1
    else:
        n = 0

    return Equality(n)


a = [1, 2, 2, 3, 4]
b = a[:] + [1, 3, 4, 4]
c = b[:] + [5]

if __name__ == '__main__':
    a_b = check_equality(a, b)
    a_c = check_equality(a, c)

    print(id(a), id(b), id(c))
    print(a, b, c)
    print(sorted(a), sorted(b), sorted(c))
    print(set(a), set(b), set(c))

    print(a_b)
    print(a_c)