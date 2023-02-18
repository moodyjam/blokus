from flask import Flask, render_template, request, url_for, jsonify
from jinja2 import Environment
from environment import Piece, Board, Game
import json
from copy import copy, deepcopy

def _enumerate(lst):
    return [(i, item) for i, item in enumerate(lst)]

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=_enumerate)

# Initialize some sample pieces and a board
green_piece = Piece("green", [[1,1,1,0,0],[0,1,0,0,0]])
blue_piece = Piece("blue", [[1,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
yellow_piece = Piece("yellow", [[1,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
pieces = [green_piece, blue_piece, yellow_piece]
board = Board(20)

game = Game(pieces = pieces, board = board)

@app.route("/")
def home():
    return render_template("home.html", board=game.board, pieces=[piece.__dict__ for piece in game.pieces])

# @app.route("/place", methods=["POST"])
# def place():
#     x = int(request.form["x"])
#     y = int(request.form["y"])
#     name = str(request.form["name"])
#     piece_index = int(request.form["piece_index"])
#     piece = pieces[piece_index]

#     board.place_piece(piece, x, y, force=True)

#     # Put the image paths into json
#     # img_paths = [piece.img_path for piece in pieces]
#     # img_paths_json = json.dumps(img_paths)

#     return render_template("home.html", pieces=pieces, board=board)

@app.route("/place", methods=["POST"])
def place():

    x = int(request.form["x"])
    y = int(request.form["y"])
    name = str(request.form["name"])

    # Find the piece with the matching name
    for piece in pieces:
        if piece.name == name:
            game.board.place_piece(piece, x, y, force=True)
            break

    # return jsonify(pieces = [piece.to_dict() for piece in pieces], board = board.to_dict())
    return render_template("home.html", board=game.board, pieces=[piece.__dict__ for piece in game.pieces])
    # return jsonify(board=game.board.__dict__, pieces=[piece.__dict__ for piece in game.pieces])

if __name__ == "__main__":
    app.run(debug=True)
