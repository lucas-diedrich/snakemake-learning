from skimage import io, color, exposure, filters
import numpy as np
import argparse


def argparser():
    """Comman line interface"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True, help="Input image")
    parser.add_argument(
        "--transformation",
        type=str,
        choices=["grayscale", "equalized", "blurred", "original"],
        help="Transformation type, must be one of grayscale, equalized, blurred",
    )

    parser.add_argument("--output", type=str, help="Output file")

    return parser.parse_args()


def main():
    args = argparser()

    image = io.imread(args.image)

    if args.transformation == "grayscale":
        result = color.rgb2gray(image)
    elif args.transformation == "equalized":
        result = exposure.equalize_hist(image)
    elif args.transformation == "blurred":
        result = filters.gaussian(image, sigma=5, channel_axis=-1)
    elif args.transformation == "original":
        result = image
    else:
        raise ValueError("Transformation not implemented")

    io.imsave(
        args.output, (result * 255).astype(np.uint8) if result.max() <= 1 else result
    )


if __name__ == "__main__":
    main()
