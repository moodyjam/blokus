class Piece:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

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

class Board:
    def __init__(self, size):
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.size = size
        self.colors = {0: ".", "red": "R", "blue": "B", "green": "G", "yellow": "Y"}

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
                        self.grid[x + i][y + j] = piece.color
            return True


    def print_board(self):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                row += self.colors[self.grid[i][j]] + " "
            print(row)

if __name__ == "__main__":
    # Example usage:
    red_piece = Piece("red", [[1, 1], [1, 1]])
    red_piece2 = Piece("red", [[1, 0], [1, 1], [0, 1]])
    # blue_piece = Piece("blue", [[1, 1], [1, 1], [0, 1]])
    # blue_piece2 = Piece("blue", [[1, 1], [1, 1]])
    board = Board(20)
    board.place_piece(red_piece, 10, 10, force=True)
    board.place_piece(red_piece2, 11, 8)
    # board.place_piece(blue_piece, 9, 8, force=True)
    # board.place_piece(blue_piece2, 12, 10)
    board.print_board()
    print()

    # # Flip the blue piece horizontally
    # blue_piece.flip_piece("horizontal")
    # board.place_piece(blue_piece, 10, 10)
    # board.print_board()
    # print()

    # # Flip the blue piece vertically
    # blue_piece.flip_piece("vertical")
    # board.place_piece(blue_piece, 15, 15)
    # board.print_board()
    # print()



