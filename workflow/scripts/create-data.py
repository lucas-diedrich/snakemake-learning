"""Get an image from skimage.data and save it to a file"""

import argparse

import numpy as np
from skimage import data
from skimage.io import imsave


def argparser():
    parser = argparse.ArgumentParser(description="Get an image from `skimage.data`")
    parser.add_argument(
        "--image-name", help="Image name. Must be a valid image from `skimage.data`"
    )
    parser.add_argument("--output", help="Save to path")

    return parser.parse_args()


def main():
    args = argparser()

    # See https://scikit-image.org/docs/stable/auto_examples/data/plot_general.html#sphx-glr-auto-examples-data-plot-general-py
    caller = getattr(data, args.image_name)
    image: np.ndarray = caller()

    imsave(
        args.output,
        image,
    )


if __name__ == "__main__":
    main()
