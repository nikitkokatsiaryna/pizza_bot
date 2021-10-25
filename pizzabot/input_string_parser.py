import re
from .input import Parser


class InputStringParser(Parser):

    def parse(self, raw_data):
        """
        Parameters
        ----------
        raw_data: str, required
           Input data

        Returns
        ----------
        width: int
        height: int
        points: list of tuples
        """

        raw_data = re.sub(r'\s+', '', raw_data)

        size_str = next(iter(re.findall(r'^-?\d+x-?\d+', raw_data)), None)

        if not size_str:
            raise Exception('There is no array size in the input data')

        point_strings = re.findall(r'\(\d+,\d+\)', raw_data)

        if not point_strings or len(point_strings) < 2:
            raise Exception('At least two points must be specified in the input data')

        # Parse dimensions
        width, height = list(map(int, size_str.split('x')))

        points = [(0, 0)]

        # Parse points
        for point_str in point_strings:
            numbers = tuple(map(int, re.findall(r'-?\d+', point_str)))
            if numbers == (0, 0):
                continue
            points.append(numbers)

        return width, height, points
