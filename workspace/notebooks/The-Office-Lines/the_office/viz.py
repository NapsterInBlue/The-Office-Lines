import matplotlib.pyplot as plt
import numpy as np

from .transform import shared_scene_matrix


def pairwise_scene_plot(castByScene):
    fig, ax = plt.subplots(figsize=(18, 10))

    chars = castByScene.columns
    scenePairs = shared_scene_matrix(castByScene)

    im = ax.imshow(scenePairs, cmap='jet')
    ax.figure.colorbar(im)

    _ = ax.set_xticks(np.arange(len(chars)))
    _ = ax.set_yticks(np.arange(len(chars)))

    _ = ax.set_xticklabels(chars, rotation=45, ha='right')
    _ = ax.set_yticklabels(chars)

    _ = ax.set_title('Number of Scenes Shared, by Character', size=20)

    return ax
