import pytest

from numbers_to_dec import list_to_decimal


def test_numbers():
    samples = {
        1: [1],
        12: [1, 2],
        123: [1, 2, 3],
        1234: [1, 2, 3, 4],
        12345: [1, 2, 3, 4, 5],
    }

    for num, lst in samples.items():
        assert list_to_decimal(lst) == num


def test_type_error():
    with pytest.raises(TypeError):
        list_to_decimal([True])
        list_to_decimal([-1])
        list_to_decimal(['a'])
        list_to_decimal([1.])

    with pytest.raises(ValueError):
        list_to_decimal([11])
