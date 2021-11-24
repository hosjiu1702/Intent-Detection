from typing import List

from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def draw_class_dist(X: List, y: List):
    """ 
    Draw classes distribution
    -----
    Args:
        X: (List) - list of data points
        y: (List) - list of targets corresponding to each data point by order.
    Returns:
        None
    """
    # Need to implement
    pass


def tsne(X, targets, title="Title", figsize=(15, 10), *args, **kwargs):
    """ Use t-SNE to visualize class distribution from the input data (X)
    in a 2-D space.

    Args:
        X: (ndarray of shape(num_samples, num_dimensions)) - Input data.
        targets: (List) - List of targets corresponding to each of the given input data points by order.
    Returns:
        None
    """
    # Maybe we need to expand more values than now.
    COLORS = [
        "#5ef3da",
        "#5ec4f3",
        "#5e72f3",
        "#925ef3",
        "#c95ef3",
        "#f35e74",
        "#f38d5e",
        "#d3f35e",
        "#557740",
        "darkorange",
        "seagreen",
        "darkslateblue",
        "black",
        "darksalmon"
    ]
    tsne = TSNE(n_components=2)
    embeddings = tsne.fit_transform(X)
    x_1 = embeddings[:, 0]
    x_2 = embeddings[:, 1]

    # colors_dict = {}
    # unique_classes = np.unique(targets)
    # for idx, c in enumerate(unique_classes):
    #     colors_dict.update({c: COLORS[idx]})
    # c = [colors_dict[target] for target in targets]
    
    colors_dict = {}
    unique_classes = np.unique(targets)
    

    # Plot scatter
    fig, ax = plt.subplots(figsize=figsize)
    scatter = plt.scatter(x_1, x_2,
                          s=13, # marker size
                          c=c) # marker color

    # Add legend
    legend = ax.legend(scatter.legend_elements()[0],
                       labels=unique_classes,
                       title=title)
    ax.add_artist(legend)

    plt.show()
