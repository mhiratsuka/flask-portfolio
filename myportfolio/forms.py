from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from myportfolio.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passoword', validators=[DataRequired(), Length(min=8, max=15)])
    confirm_password = PasswordField('Confirm Passowrd', validators=[DataRequired(), EqualTo('password')])
    submit =SubmitField('Sign Up')

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user: 
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email): 
        email = User.query.filter_by(email=email.data).first()
        if email: 
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passowrd', validators=[DataRequired(), Length(min=8, max=15)])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit =SubmitField('Update')

    def validate_username(self, username): 
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user: 
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email): 
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email: 
                raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    worktitle = StringField('Title', validators=[DataRequired()])
    skill = TextAreaField('Skill', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    submit =SubmitField('Request Password Reset')

    def validate_email(self, email): 
        email = User.query.filter_by(email=email.data).first()
        if email is None: 
            raise ValidationError('There is no acout with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Passoword', validators=[DataRequired(), Length(min=8, max=15)])
    confirm_password = PasswordField('Confirm Passowrd', validators=[DataRequired(), EqualTo('password')])
    submit =SubmitField('Reset Password')

