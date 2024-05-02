from flask import Flask, Blueprint, render_template
from pybo.models import Question

bp = Blueprint("board", __name__, url_prefix="/board")


@bp.route("/list")
def list():
    question_list= Question.query.order_by(Question.create_date.desc())
    return render_template("board/board_list.html", question_list=question_list)

