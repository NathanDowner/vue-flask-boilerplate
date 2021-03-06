from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired


class GenericForm(FlaskForm):
    field1 = StringField('field1', validators=[InputRequired()])
    field2 = TextAreaField('field2', validators=[InputRequired()])
    field3 = FileField('field3', validators=[FileRequired(),  FileAllowed(['jpg','jpeg', 'png', 'Only images are accepted!'])])
    