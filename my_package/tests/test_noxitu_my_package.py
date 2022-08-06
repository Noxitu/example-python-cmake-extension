import noxitu.my_package as my_package


def test_mul_int():
    assert my_package.mul(2, 3) == 6


def test_mul_float():
    assert abs(my_package.mul(1 / 2, 1 / 3) - 1 / 6) < 1e-6
