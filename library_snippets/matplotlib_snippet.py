import matplotlib.pyplot as plt
from typing import List, Any

def plot_line(x_data: List[Any], y_data: List[Any], title: str, x_label: str, y_label: str, line_style: str = '-', color: str = 'blue'):
    plt.plot(x_data, y_data, line_style, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_bar(x_data: List[Any], y_data: List[Any], title: str, x_label: str, y_label: str, color: str = 'blue'):
    plt.bar(x_data, y_data, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_scatter(x_data: List[Any], y_data: List[Any], title: str, x_label: str, y_label: str, color: str = 'blue'):
    plt.scatter(x_data, y_data, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_histogram(data: List[Any], bins: int, title: str, x_label: str, y_label: str, color: str = 'blue'):
    plt.hist(data, bins=bins, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_pie(sizes: List[float], labels: List[str], title: str, colors: List[str] = None):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title(title)
    plt.show()
