from .output import Output


class ConsoleOutput(Output):

    def print_result(self, value):
        print(value)

    def print_error(self, error):
        print(f"Error: {error}")
