# Slice Code Challenge

## Pizzabot

Pizzabot is a robbot, that helps you to deliver pizzas to all the houses in a neighborhood. To do this, you simply give an
instruction to which house to make the delivery

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```
pip install -r requirements.txt 
```

## Usage

To run the script use the next command in the command line

```
python pizzabot.py "<size> <points>"

# where size - the size of your array (e.g. '5x5')
#       points - coordinates of houses on the grid (e.g. (1, 3) (4, 4))
```

After executing the script, you will get a string of capital letters, according to the following instructions

```
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza
```

Therefore, given the following input:

```
$ python pizzabot.py "5x5 (1, 3) (4, 4)"
```

one correct solution would be:

```
ENNNDEEEND
```

It means: move east once and north thrice; drop a pizza; move east thrice and north once; drop a final pizza.

## Tests

To run tests use the following command in the command line

```
python pizzabot_test.py
```
