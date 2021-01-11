from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextInput


class BlogPostForm(FlaskForm):

    title = StringField('Whats on your mind : ', validators=[DataRequired()])
    text = TextAreaField('Tell us more about it : ', validators=[DataRequired()])
    submit = SubmitField('Spread the word')
