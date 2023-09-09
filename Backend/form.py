from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Form_validation(FlaskForm):
    slack_name = StringField("Slack_Name", validators=[DataRequired()])
    track = StringField("Track", validators=[DataRequired()])
