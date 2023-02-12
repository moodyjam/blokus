from flask import Flask, render_template, request
from jinja2 import Environment
from environment import Piece, Board

def _enumerate(lst):
    return [(i, item) for i, item in enumerate(lst)]

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=_enumerate)

# Initialize some sample pieces and a board
green_piece = Piece("green", [[1, 1], [1, 1]])
blue_piece = Piece("blue", [[1, 1, 1], [0, 1, 0]])
red_piece = Piece("red", [[1, 1, 1], [1, 0, 0]])
yellow_piece = Piece("yellow", [[1, 1, 0], [0, 1, 1]])
pieces = [green_piece, blue_piece, red_piece, yellow_piece]
board = Board(20)

@app.route("/")
def home():
    return render_template("home.html", board=board, pieces=pieces)

@app.route("/place", methods=["POST"])
def place():
    x = int(request.form["x"])
    y = int(request.form["y"])
    piece_index = int(request.form["piece_index"])
    piece = pieces[piece_index]

    board.place_piece(piece, x, y, force=True)

    return render_template("home.html", pieces=pieces, board=board)

if __name__ == "__main__":
    app.run(debug=True)
