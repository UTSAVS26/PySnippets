from package.show import display
from package.write import plot


def write(snippet_name, password):
    return plot(snippet_name, password)


def show(snippet_name, password, clipboard=None):
    return display(snippet_name, password, clipboard=None)
