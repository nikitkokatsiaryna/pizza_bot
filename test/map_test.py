import pytest
from pizzabot.map import Map


def test_big_points():
    with pytest.raises(Exception) as error:
        Map(width=5, height=5, points=[(10, 3), (2, 4)])
    assert 'The points (10, 3) are more than the array size' == error.value.args[0]
