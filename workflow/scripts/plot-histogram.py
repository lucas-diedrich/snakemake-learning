"""Plot pixel-intensity histogram of a grayscale or RGB image"""

import argparse
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from typing import Any


def argparser():
    """Command line interface"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, help="Input image")
    parser.add_argument("--title", type=str, help="Title", required=True)
    parser.add_argument("--output", type=str, help="Output file")

    return parser.parse_args()


def plot_histogram(
    image: np.ndarray,
    title: str | None = None,
    save: str | None = None,
    *,
    return_fig: bool = False,
) -> Any:
    """Plot histogram of a grayscale or RGB image"""
    if image.ndim == 2:
        COLORS = ["#cccccc"]
        image = np.expand_dims(image, axis=-1)
    else:
        COLORS = ["#ff0000", "#00ff00", "#0000ff"]

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))

    for channel in range(image.shape[-1]):
        data = image[..., channel].ravel()
        ax.hist(
            data,
            bins=256,
            color=COLORS[channel],
            label=COLORS[channel],
        )

    if title is not None:
        ax.set_title(title)

    ax.legend()
    plt.tight_layout()

    if save is not None:
        plt.savefig(save, bbox_inches="tight")

    if return_fig:
        return fig

    plt.close()


def main():
    args = argparser()

    image = io.imread(args.image)

    plot_histogram(image, title=args.title, save=args.output)


if __name__ == "__main__":
    main()
