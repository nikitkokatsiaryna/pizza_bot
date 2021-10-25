from .point import Point


class Map:
    """
    The class checks that the array sizes are greater than zero.

    The class takes the dimensions of the array and coordinates
    and checks whether the coordinates are within the limits
    of the input array. Otherwise, an exception is triggered
    """

    def __init__(self, **opts):
        self.width = None
        self.height = None
        self.points = []

        self.set_attrs(**opts)

    def set_attrs(self, **attrs):
        width = attrs.get('width', None)

        if width:
            self.set_width(width)

        height = attrs.get('height', None)

        if height:
            self.set_height(height)

        points = attrs.get('points', [])

        if points:
            self.set_points(points)

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        if new_height <= 0:
            raise Exception('Field height should be more than 0')

        self.height = new_height

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        if new_width <= 0:
            raise Exception('Field width should be more than 0')

        self.width = new_width

    def get_points(self):
        return self.points

    def get_last_point(self):
        return self.points[-1]

    def set_points(self, new_points):
        if not self.height or not self.width:
            raise Exception("You should specify field height and width first")

        for point_x, point_y in new_points:
            is_point_x_in_field = self.width >= point_x >= 0
            is_point_y_in_field = self.height >= point_y >= 0

            if not is_point_x_in_field or not is_point_y_in_field:
                raise Exception(f'The points {point_x, point_y} are more than the array size')

        self.points = list(map(lambda p: Point(*p), new_points))
