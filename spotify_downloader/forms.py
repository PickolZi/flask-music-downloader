from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, widgets
from wtforms.validators import data_required, input_required
from wtforms.fields import SelectMultipleField

class SpotifySongDownloadForm(FlaskForm):
    url = StringField('url', [data_required()])
    submit = SubmitField('submit')

class SpotifyGetUser(FlaskForm):
    user = StringField('user_id', [data_required()])
