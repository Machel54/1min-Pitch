from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    categories_id = SelectField('Select Category', choices=[('1', 'product'),  ('2', 'Interview'),('3','Promotion')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')
