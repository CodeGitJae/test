from flask import Flask, Blueprint, render_template,session, request, url_for, g, flash
from pybo.models import Question, User
from pybo.forms import QuestionForm, AnswerForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect

bp = Blueprint("board", __name__, url_prefix="/board")


@bp.route("/update/<int:question_id>", methods=("GET","POST"))
def update(question_id):
    question = Question.query.get_or_404((question_id))
    
    if g.user != question.user:
        flash("수정 권한이 없습니다.")
        return redirect(url_for('board.board_detail', question_id=question_id))
    
    if request.method == 'POST':
        form = QuestionForm()

        if form.validate_on_submit():
            form.populate_obj(question)
            question.update_date = datetime.now()
            db.session.commit()

            return redirect(url_for('board.board_detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)

    return render_template("board/create_form.html", form=form) 

@bp.route("/detail/<int:question_id>", methods=("GET","POST"))
def board_detail(question_id):
    form = AnswerForm()

    question = Question.query.get(question_id)

    return render_template("board/board_detail.html", question=question, form=form)


@bp.route("/create", methods=('GET','POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():
        
        subject = form.subject.data
        content = form.content.data
        create_date = datetime.now()
        user_id = form.user_id.data
        question = Question(subject=subject, content=content, create_date=create_date, user_id=user_id)

        db.session.add(question)
        db.session.commit()

        return redirect(url_for("board.list"))


    return render_template("board/create_form.html", form=form)


@bp.route("/nickname")
def nickname():

    users = User.query.all()
    nicknames = [user.nickname for user in users]
    
    return render_template("board/user_nickname.html", nicknames=nicknames)
    

@bp.route("/list")
def list():
    question_list= Question.query.order_by(Question.create_date.desc())
    funimg =[
        "/others/fun1.jpg",
        "/others/fun2.png",
        "/others/fun3.jpg"
    ]

    return render_template('board/board_list.html', question_list=question_list, funimg=funimg)


