# flake8: noqa

"""
Keyword arguments are one of those Python features that often seems a little odd for folks moving to Python from many other programming languages. It doesn’t help that folks learning Python often discover the various features of keyword arguments slowly over time.

https://treyhunner.com/2018/04/keyword-arguments-in-python/

"""

from math import sqrt


def quadratic(a, b, c):
    x1 = -b / (2 * a)
    x2 = sqrt(b**2 - 4 * a * c) / (2 * a)
    return (x1 + x2), (x1 - x2)


# We can pass our arguments as positional arguments like this:
quadratic(31, 93, 62)

# Or we can pass our arguments as keyword arguments like this:
quadratic(a=31, b=93, c=62)
