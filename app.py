from boggle import Boggle
from flask import Flask, request, render_template, redirect, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "boogle-bop"

boggle_game = Boggle()

@app.route("/root")
def home():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplay =session.get("nplays", 0)

    return render_template("index.html", board=board, numplay=numplay, highscore=highscore)

@app.route("/post-score", methods=["POST"])
def postscore():
    score = request.json['score']
    highscore =session.get("highscore", 0)
    numplay = session.get("nplays", 0)

    session['numplay'] = numplay + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord= score > highscore)