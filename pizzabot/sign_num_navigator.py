class SignNumNavigator:

    def find_route(self, p_map):
        """
        :param p_map: an object containing width: int, height: int, points: list
        :return: str
        """

        direction = ''
        points = p_map.get_points()
        last_point = p_map.get_last_point()

        for index, cur_point in enumerate(points):
            if cur_point == last_point:
                continue

            next_point = points[index + 1]
            x, y = self._get_distance(cur_point, next_point)

            direction += ''.join([
                'E' * self._pos_sign(x) * x,
                'N' * self._pos_sign(y) * y,
                'W' * self._neg_sign(x) * abs(x),
                'S' * self._neg_sign(y) * abs(y),
                'D'
            ])
        return direction

    def _get_distance(self, point1, point2):
        return point2.x - point1.x, point2.y - point1.y

    def _pos_sign(self, num):
        return 1 if num > 0 else 0

    def _neg_sign(self, num):
        return 1 if num < 0 else 0
