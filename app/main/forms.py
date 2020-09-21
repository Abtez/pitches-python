from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    my_category = SelectField('Category', choices=[('Marketing','Marketing'),('Promotional','Promotional'),('Scholarship','Scholarship')],validators=[Required()])
    my_pitches = TextAreaField('Enter Pitch', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave Your Comments Below..', validators=[Required()])
    submit = SubmitField('Submit Comments')
    
class BioForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')