from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserCreateForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=5, max=20)])
    nickname = StringField('닉네임', validators=[DataRequired(), Length(min=2, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo("password2", "비밀번호가 일치하지 않음")])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField("이메일", validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])