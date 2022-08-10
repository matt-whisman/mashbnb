from app.blueprints.main.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TopCitiesSearchForm(FlaskForm):
    state = StringField('State Abbrev.', validators=[DataRequired()])
    submit = SubmitField('Get Top Citites')
