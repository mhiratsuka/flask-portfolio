from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    worktitle = StringField('Title', validators=[DataRequired()])
    category = TextAreaField('Category', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    workpicture = FileField('Content', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Post')
