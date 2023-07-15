from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, input_required

class SpotifySongDownloadForm(FlaskForm):
    url = StringField('url', [data_required()])
    submit = SubmitField('submit')