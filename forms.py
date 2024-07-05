from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class imageform(FlaskForm):
    imagefile = FileField('Upload Image file', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')