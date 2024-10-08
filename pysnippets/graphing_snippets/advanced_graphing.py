import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import logging
import scipy.stats as stats

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration dictionary
config = {
    'default_style': 'default',
    'default_figsize': (10, 6),
    'default_color_palette': 'viridis'
}

def set_config(style=None, figsize=None, color_palette=None):
    global config
    if style:
        if style in plt.style.available:
            config['default_style'] = style
        else:
            logger.warning(f"Style '{style}' not available. Using default style.")
    if figsize:
        config['default_figsize'] = figsize
    if color_palette:
        config['default_color_palette'] = color_palette

def apply_config():
    try:
        if config['default_style'] != 'default':
            plt.style.use(config['default_style'])
        plt.rcParams['figure.figsize'] = config['default_figsize']
        sns.set_palette(config['default_color_palette'])
    except Exception as e:
        logger.error(f"Error applying configuration: {str(e)}")
        logger.info("Reverting to default matplotlib style")
        plt.style.use('default')

def get_available_styles():
    return plt.style.available

def line_plot(x, y, title="Line Plot", xlabel="X-axis", ylabel="Y-axis", interactive=False):
    apply_config()
    if interactive:
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
        return fig
    else:
        plt.figure()
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

def bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values"):
    apply_config()
    plt.figure()
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

def scatter_plot(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    apply_config()
    plt.figure()
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def pie_chart(labels, sizes, title="Pie Chart"):
    apply_config()
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(title)
    plt.show()

def subplot(plot_funcs, nrows, ncols, titles):
    apply_config()
    fig, axs = plt.subplots(nrows, ncols, figsize=(5*ncols, 5*nrows))
    axs = axs.flatten()
    for ax, plot_func, title in zip(axs, plot_funcs, titles):
        plt.sca(ax)
        plot_func()
        plt.title(title)
    plt.tight_layout()
    plt.show()

def heatmap(data, title="Heatmap"):
    apply_config()
    plt.figure()
    sns.heatmap(data, annot=True, cmap="YlGnBu")
    plt.title(title)
    plt.show()

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def moving_average(data, window):
    return np.convolve(data, np.ones(window), 'valid') / window

def set_color_palette(palette):
    sns.set_palette(palette)

def annotate_point(x, y, text):
    plt.annotate(text, (x, y), xytext=(5, 5), textcoords='offset points')

def qq_plot(data, title="Q-Q Plot"):
    apply_config()
    plt.figure()
    stats.probplot(data, dist="norm", plot=plt)  # Use scipy.stats.probplot
    plt.title(title)
    plt.show()

def safe_plot(plot_func, *args, **kwargs):
    try:
        plot_func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Error in plotting: {str(e)}")
        raise