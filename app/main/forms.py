from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    category = SelectField('Category', choices=[('Marketing','Marketing'),('Promotional','Promotional'),('Scholarship','Scholarship')],validators=[Required()])
    pitch = TextAreaField('Enter Pitch', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave Your Comments Below..', validators=[Required()])
    submit = SubmitField('Submit Comments')