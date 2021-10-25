from pizzabot.sign_num_navigator import SignNumNavigator
from pizzabot.map import Map
from pizzabot.point import Point


def test_distance():
    expected_data = (3, 1)
    actual_data = SignNumNavigator()._get_distance(Point(1, 3), Point(4, 4))
    assert expected_data == actual_data


def test_negative_point_distance():
    expected_data = (5, 1)
    actual_data = SignNumNavigator()._get_distance(Point(-1, 3), Point(4, 4))
    assert expected_data == actual_data


def test_multi_points_route():
    expected = 'EEENDSSDDWWWWSDEEENDNWDEESSD'
    p_map = Map(width=4, height=4, points=[(1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2), (2, 3), (4, 1)])
    actual = SignNumNavigator().find_route(p_map)
    assert expected == actual


def test_only_drop_pizza():
    expected = 'EEEND'
    p_map = Map(width=4, height=4, points=[(1, 3), (4, 4)])
    actual = SignNumNavigator().find_route(p_map)
    assert expected == actual
