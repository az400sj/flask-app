import pytest

from src.dummy import add


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (1, 2, 3),
        (1.2, 2.3, 3.5),
        (1, 2.3, 3.3),
        (1.5, 2.5, 4),
    ],
)
def test_dummy(x, y, expected):
    result = add(x, y)
    assert result == expected
