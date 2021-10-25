from pizzabot.input_string_parser import InputStringParser


def test_parse_input_data_couple_points():
    expected_data = (5, 5, [(0, 0), (1, 3), (4, 4)])
    actual_data = InputStringParser().parse('5x5 (1, 3) (4, 4)')
    assert expected_data == actual_data


def test_parse_input_data_multi_points():
    expected_data = (5, 5, [(0, 0), (1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2), (2, 3)])
    actual_data = InputStringParser().parse('5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3)')
    assert expected_data == actual_data
