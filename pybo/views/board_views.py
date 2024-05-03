from flask import Flask, Blueprint, render_template,session
from pybo.models import Question, User

bp = Blueprint("board", __name__, url_prefix="/board")


@bp.route("/nickname")
def nickname():

    users = User.query.all()
    nicknames = [user.nickname for user in users]
    
    return render_template("board/user_nickname.html", nicknames=nicknames)
    

@bp.route("/list")
def list():

    return render_template('board/board_list.html')


