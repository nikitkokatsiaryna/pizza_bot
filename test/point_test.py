from pizzabot.point import Point


def test_equal():
    point1 = Point(1, 2)
    point2 = Point(2, 3)
    point3 = Point(2, 3)

    assert point1 != point2
    assert point2 == point3
