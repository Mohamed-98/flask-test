from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        x="this is test 1 for jinja"
    )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index)
    except IndexError:
        abort(404)
