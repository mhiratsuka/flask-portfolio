from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    worktitle = StringField('Title', validators=[DataRequired()])
    category = TextAreaField('Category', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    workpicture = FileField('Work Picture', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    workpicture_name = TextAreaField('Work Picture Name', validators=[DataRequired()])
    submit = SubmitField('Post')
