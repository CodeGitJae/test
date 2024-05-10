from flask import Flask, Blueprint, render_template, request, url_for
from pybo.models import Answer, Question
from pybo.forms import AnswerForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect

bp = Blueprint("answer", __name__, url_prefix="/answer")

@bp.route("/create/<int:question_id>", methods=("POST",))
def create_answer(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)

    if request.method == 'POST' and form.validate_on_submit():
        content = request.form["content"]
        create_date = datetime.now()
        user_id = request.form["user_id"]

        answer = Answer(question=question, content=content, 
                        create_date=create_date, user_id=user_id)

        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('board.board_detail', question_id=question.id))

    return render_template("board/board_detail.html", question=question, form=form)