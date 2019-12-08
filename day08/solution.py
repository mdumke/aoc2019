"""Process a space image."""

import sys
import numpy as np
import matplotlib.pyplot as plt
from image import check_corruption, decode_image

if __name__ == '__main__':
    digits = np.array(list(sys.stdin.readline().rstrip()), dtype=np.int8)
    print('part 1', check_corruption(digits, 25, 6))

    digits = np.array(digits)
    decoded = decode_image(digits, 25, 6)
    print('part 2', decoded)
    plt.imshow(decoded)
    plt.show()
