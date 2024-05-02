from flask import Flask, Blueprint, render_template, request, session, g
from pybo.models import Question, User

bp = Blueprint("main", __name__, url_prefix="/")

@bp.before_app_request
def play_g():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None

    else:
        g.user = User.query.get(user_id)


@bp.route("/")
def index():

    return render_template("board/board_list.html")
