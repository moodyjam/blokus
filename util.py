
import itertools

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import os


def reduce_shape(array):
    # Remove all-zero rows
    array = array[~np.all(array == 0, axis=1)]
    # Remove all-zero columns
    array = array[:, ~np.all(array == 0, axis=0)]
    return array

def get_binary(piece_array):
    flat = list(itertools.chain.from_iterable(piece_array))
    binary = "".join(map(str, flat))
    return binary


def generate_piece_image(piece_array, color, save_path):

    array = reduce_shape(np.array(piece_array))

    binary = get_binary(piece_array)

    fig, ax = plt.subplots()
    fig.set_size_inches(array.shape[1],array.shape[0])
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if piece_array[i][j]:
                ax.add_patch(patches.Rectangle((j, array.shape[0] - i - 1), 1, 1, edgecolor='black', facecolor=color))
    
    ax.axis('off')  
    ax.set_ylim([0, array.shape[0]])
    ax.set_xlim([0, array.shape[1]])
    plt.savefig(save_path, bbox_inches='tight')


if __name__ == "__main__":
    # Example usage
    generate_piece_image([[1,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]], 'blue')


