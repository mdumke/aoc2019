import numpy as np
from collections import Counter


def check_corruption(digits, width, height):
    """Return number of 1s times number of 2s in layer with least 0s."""
    layers = digits.reshape((-1, width * height))
    fewest_zeros_layer = layers[np.argmax(np.count_nonzero(layers, axis=1))]
    counts = Counter(fewest_zeros_layer)
    return counts[1] * counts[2]


def decode_image(digits, width, height):
    """Return image with first non-transparent layer-values for each pixel."""
    def keep_first_non_transparent(values):
        for digit in values:
            if digit != 2:
                return digit
        return 2

    img = np.dstack(digits.reshape((-1, height, width)))
    return np.apply_along_axis(keep_first_non_transparent, 2, img)


