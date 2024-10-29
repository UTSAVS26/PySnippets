import matplotlib.pyplot as plt

def plot_line(x_data, y_data, title, x_label, y_label):
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_bar(x_data, y_data, title, x_label, y_label):
    plt.bar(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_scatter(x_data, y_data, title, x_label, y_label):
    plt.scatter(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_histogram(data, bins, title, x_label, y_label):
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_pie(sizes, labels, title):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
