from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    category = StringField('Pitch Category', validators=[Required()])
    pitch = TextAreaField('Enter Review')
    submit = SubmitField('Submit')