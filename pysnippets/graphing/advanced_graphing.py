import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import logging
import scipy.stats as stats
from dataclasses import dataclass
from typing import Callable, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class GraphConfig:
    style: str = 'default'
    figsize: tuple = (10, 6)
    color_palette: str = 'viridis'

# Global configuration instance
config = GraphConfig()

def set_config(style: str = 'default', figsize: tuple = (10, 6), color_palette: str = 'viridis') -> None:
    """Set global configuration for plotting."""
    global config
    if style not in plt.style.available:
        logger.warning(f"Invalid style '{style}' provided. Defaulting to 'default'.")
        style = 'default'
        
    config.style = style
    config.figsize = figsize
    config.color_palette = color_palette
    plt.style.use(style)
    
    # Validate color palette
    if color_palette in sns.palettes.SEABORN_PALETTES.keys():
        sns.set_palette(color_palette)
    else:
        logger.warning(f"Invalid color palette '{color_palette}' provided. Defaulting to 'viridis'.")
        sns.set_palette('viridis')

def get_available_styles() -> list:
    """Returns a list of available matplotlib styles."""
    return plt.style.available

def apply_config() -> None:
    """Applies the current configuration settings."""
    try:
        plt.style.use(config.style if config.style != 'default' else 'default')
        plt.rcParams['figure.figsize'] = config.figsize
        sns.set_palette(config.color_palette)
    except Exception as e:
        logger.error(f"Error applying configuration: {str(e)}")
        logger.info("Reverting to default matplotlib style")
        plt.style.use('default')

def safe_plot(plot_func: Callable[..., None], *args: Any, **kwargs: Any) -> None:
    """Safely executes a plotting function with error handling."""
    try:
        plot_func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Error in plotting: {str(e)}")
        raise

def line_plot(x: np.ndarray, y: np.ndarray, title: str = "Line Plot", xlabel: str = "X-axis", ylabel: str = "Y-axis", interactive: bool = False) -> None:
    """Creates a line plot."""
    apply_config()
    if interactive:
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
        fig.show()
    else:
        plt.figure()
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

def bar_chart(categories: list, values: list, title: str = "Bar Chart", xlabel: str = "Categories", ylabel: str = "Values") -> None:
    """Creates a bar chart."""
    apply_config()
    plt.figure()
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

def scatter_plot(x: np.ndarray, y: np.ndarray, title: str = "Scatter Plot", xlabel: str = "X-axis", ylabel: str = "Y-axis") -> None:
    """Creates a scatter plot."""
    apply_config()
    plt.figure()
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def pie_chart(labels: list, sizes: list, title: str = "Pie Chart") -> None:
    """Creates a pie chart."""
    apply_config()
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(title)
    plt.show()

def subplot(plot_funcs: list, nrows: int, ncols: int, titles: list) -> None:
    """Creates subplots from a list of plotting functions."""
    apply_config()
    fig, axs = plt.subplots(nrows, ncols, figsize=(5*ncols, 5*nrows))
    axs = axs.flatten()
    for ax, plot_func, title in zip(axs, plot_funcs, titles):
        plt.sca(ax)
        plot_func()
        plt.title(title)
    plt.tight_layout()
    plt.show()

def heatmap(data: np.ndarray, title: str = "Heatmap") -> None:
    """Creates a heatmap."""
    apply_config()
    plt.figure()
    sns.heatmap(data, annot=True, cmap="YlGnBu")
    plt.title(title)
    plt.show()

def normalize_data(data: np.ndarray) -> np.ndarray:
    """Normalizes the data to a range of [0, 1]."""
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def moving_average(data: np.ndarray, window: int) -> np.ndarray:
    """Calculates the moving average of the data."""
    return np.convolve(data, np.ones(window), 'valid') / window

def set_color_palette(palette: str) -> None:
    """Sets the color palette for plots."""
    sns.set_palette(palette)

def annotate_point(x: float, y: float, text: str) -> None:
    """Annotates a point on the plot."""
    plt.annotate(text, (x, y), xytext=(5, 5), textcoords='offset points')

def qq_plot(data: np.ndarray, title: str = "Q-Q Plot") -> None:
    """Creates a Q-Q plot."""
    apply_config()
    plt.figure()
    stats.probplot(data, dist="norm", plot=plt)
    plt.title(title)
    plt.show()
