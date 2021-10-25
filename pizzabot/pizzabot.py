class Pizzabot:

    def __init__(self, input_manager, output_manager, map_obj, navigator):
        self.input_manager = input_manager
        self.output_manager = output_manager
        self.map = map_obj
        self.navigator = navigator

    def start(self, input_str):
        try:
            width, height, points = self.input_manager.parse(input_str)
            self.map.set_attrs(width=width, height=height, points=points)
            direction = self.navigator.find_route(self.map)
            self.output_manager.print_result(direction)
        except Exception as error:
            self.output_manager.print_error(error)
