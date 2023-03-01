from util import *
import numpy as np
from copy import copy

class Game:
    def __init__(self, pieces, board):
        self.pieces = pieces
        self.board = board
        self.board_copy = copy(board)

class Piece:
    def __init__(self, color, shape, root_dir="./static/pics", name=None):
        self.color = color
        self.shape = shape

        if name is None:
            self.name = f"{self.color}_{get_binary(shape)}"
        else:
            self.name = name

        # Create pics if they don't exist. Then save the image path
        if root_dir is not None:
            self.img_path = os.path.join(root_dir, f"{self.name}.png")
            if not os.path.exists(self.img_path):
                generate_piece_image(self.shape, self.color, self.img_path)

    def rotate_piece(self):
        n = len(self.shape)
        m = len(self.shape[0])
        rotated_shape = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            for j in range(m):
                rotated_shape[j][n - i - 1] = self.shape[i][j]
        self.shape = rotated_shape

    def flip_piece(self, direction):
        if direction == "horizontal":
            self.shape = [row[::-1] for row in self.shape]
        elif direction == "vertical":
            self.shape = self.shape[::-1]

    def to_dict(self):
        return {"color": self.color, 
                "shape": self.shape,
                "name": self.name}


class Board:
    def __init__(self, size, grid=None, colors=None):
        
        self.size = size

        if grid is None:
            self.grid = [["white" for i in range(size)] for j in range(size)]

        if colors is None:
            self.colors = {"white": ".", "red": "R", "blue": "B", "green": "G", "yellow": "Y"}

    def valid_place_piece(self, piece, x, y):
        valid_placement = False
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[0])):
                if piece.shape[i][j] == 1:

                    # Make placement is not off the board
                    if (
                        x + i < 0
                        or x + i >= self.size
                        or y + j < 0
                        or y + j >= self.size
                    ):
                        print(1)
                        return False

                    # Make sure no pieces overlap
                    if (
                        self.grid[x + i][y + j] != 0
                    ):
                        print(2)
                        return False

                    # Cannot be directly adjacent to a piece of the same color
                    if x + i - 1 > 0 and self.grid[x + i - 1][y + j] == piece.color:
                        print(3)
                        return False
                    if x + i + 1 < self.size and self.grid[x + i + 1][y + j] == piece.color:
                        print(4)
                        return False
                    if y + j + 1 < self.size and self.grid[x + i][y + j + 1] == piece.color:
                        print(5)
                        return False
                    if y + j - 1 > 0 and self.grid[x + i][y + j - 1] == piece.color:
                        print(6)
                        return False

                    # Check to make sure the corners match ups
                    if x + i - 1 > 0 and y + j - 1 > 0 and self.grid[x + i - 1][y + j - 1] == piece.color:
                        print(7)
                        valid_placement = True
                    if x + i + 1 < self.size and y + j - 1 > 0 and self.grid[x + i + 1][y + j - 1] == piece.color:
                        print(8)
                        valid_placement = True
                    if x + i - 1 > 0 and y + j + 1 < self.size and self.grid[x + i - 1][y + j + 1] == piece.color:
                        print(9)
                        valid_placement = True
                    if x + i + 1 < self.size and y + j + 1 < self.size and self.grid[x + i + 1][y + j + 1] == piece.color:
                        print(10)
                        valid_placement = True
        return valid_placement

    def place_piece(self, piece, x, y, force=False):
        if self.valid_place_piece(piece, x, y) or force:
            for i in range(len(piece.shape)):
                for j in range(len(piece.shape[0])):
                    if piece.shape[i][j] == 1:
                        try:
                            self.grid[x + i][y + j] = piece.color
                        except IndexError:
                            return False
            return True


    def print_board(self):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                row += self.colors[self.grid[i][j]] + " "
            print(row)

def parse_blocks(file_name , rows, columns):   #for blocks.txt, rows = 3 columns =5
    #this parses
    game = {}
    with open("blocks.txt", 'r') as file:
        blocks = file.read().split('\n')
        for block in blocks:
            if block != '':
                block = block.split(" ")
                color = block.pop(0)
                block = [int(i) for i in block]
                array = [block[columns*i: columns*(i+1)] for i in range(rows)]
                piece = Piece(color, array)

                if color not in game:
                    game[color] = []
                
                game[color].append(piece)
    
    return game

            


if __name__ == "__main__":
    game = parse_blocks("blocks.txt", rows = 3, columns = 5)
    # Example usage:
    # red_piece = Piece("red", [[1, 1], [1, 1]])
    # red_piece2 = Piece("red", [[1, 0], [1, 1], [0, 1]])

    red_piece = game['blue'][19]
    
    # blue_piece = Piece("blue", [[1, 1], [1, 1], [0, 1]])
    # blue_piece2 = Piece("blue", [[1, 1], [1, 1]])
    board = Board(20)
    board.place_piece(red_piece, 15, 17, force = True)
    # board.place_piece(red_piece2, 11, 8)
    # board.place_piece(blue_piece, 9, 8, force=True)
    # board.place_piece(blue_piece2, 12, 10)
    # board.print_board()

    # # Flip the blue piece horizontally
    # red_piece.flip_piece("horizontal")
    board.place_piece(red_piece, 10, 10)
    board.print_board()
    # print()

    # # Flip the blue piece vertically
    # blue_piece.flip_piece("vertical")
    # board.place_piece(blue_piece, 15, 15)
    # board.print_board()
    # print()




