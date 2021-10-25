import sys
from pizzabot.pizzabot import Pizzabot
from pizzabot.map import Map
from pizzabot.input_string_parser import InputStringParser
from pizzabot.console_output import ConsoleOutput
from pizzabot.sign_num_navigator import SignNumNavigator


if __name__ == '__main__':
    pizzabot = Pizzabot(
        InputStringParser(),
        ConsoleOutput(),
        Map(),
        SignNumNavigator()
    )

    pizzabot.start(''.join(sys.argv[1:]))
