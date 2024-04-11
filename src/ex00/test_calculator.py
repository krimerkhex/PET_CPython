import pytest
import calculator


@pytest.mark.parametrize(["a", "b"], [(1, 2)])
def test_calc_1(a, b):
    assert calculator.add(a, b) == 3


@pytest.mark.parametrize(["a", "b"], [(1, 2)])
def test_calc_1(a, b):
    assert calculator.sub(b, a) == 1


@pytest.mark.parametrize(["a", "b"], [(1, 2)])
def test_calc_1(a, b):
    assert calculator.mul(a, b) == 2


@pytest.mark.parametrize(["a", "b"], [(1, 2)])
def test_calc_1(a, b):
    assert calculator.div(b, a) == 0.5


@pytest.mark.parametrize(["a", "b"], [(1, 0)])
def test_calc_1(a, b):
    try:
        calculator.div(a, b)
        assert False
    except ZeroDivisionError:
        assert True
