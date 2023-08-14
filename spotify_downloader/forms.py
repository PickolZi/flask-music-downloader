from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, widgets
from wtforms.validators import data_required, input_required

class SpotifySongDownloadForm(FlaskForm):
    input = StringField('url', [data_required()], render_kw={'placeholder': 'Enter Spotify user id: '})
    submit = SubmitField('Search')

class SpotifyGetUser(FlaskForm):
    user = StringField('user_id', [data_required()])
