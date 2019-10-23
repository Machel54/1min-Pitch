from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    categories_id = SelectField('Select Category', choices=[('1', 'product'),  ('2', 'Interview'),('3','Promotion')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  
