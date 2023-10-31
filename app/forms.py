from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddNoteForm( FlaskForm ):
    title = StringField( "Title", validators=[ DataRequired() ] )
    submit = SubmitField( 'Submit' )


class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')