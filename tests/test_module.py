import myproject.module


def test_add() -> None:
    assert myproject.module.add(3, 4) == 7


def test_sub() -> None:
    assert myproject.module.sub(10, 9) == 1
