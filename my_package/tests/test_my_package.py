import my_package


def test_add_int():
    assert my_package.add(2, 3) == 5


def test_add_float():
    assert abs(my_package.add(1 / 2, 1 / 3) - 5 / 6) < 1e-6
