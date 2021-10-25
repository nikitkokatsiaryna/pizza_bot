class Point:
    """
    initializing points
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        if type(point) != Point:
            super()

        return self.x == point.x and self.y == point.y
