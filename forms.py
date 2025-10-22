from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import SelectField, FileField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(max=200)])
    is_teacher = BooleanField('Я преподаватель')
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
    

class HWUploadForm(FlaskForm):
    teacher_id = SelectField('Преподаватель', coerce=int, validators=[DataRequired()])
    file = FileField('Файл с домашкой', validators=[DataRequired()])
    submit = SubmitField('Отправить')
    
class ReviewForm(FlaskForm):
    grade = StringField('Оценка', validators=[DataRequired()])
    feedback = TextAreaField('Комментарий', validators=[Length(max=2000)])
    submit = SubmitField('Сохранить отзыв')
