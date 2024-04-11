import pytest
from multiply import mul


def test_multiply():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    y = [[1, 2], [1, 2], [3, 4]]
    result = mul(x, y)
    assert result == [[12, 18], [27, 42], [42, 66], [57, 90]]



