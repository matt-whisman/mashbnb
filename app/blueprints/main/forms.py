from app.blueprints.main.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StateSearchForm(FlaskForm):
    state = StringField('State Abbrev.', validators=[DataRequired()])
    submit = SubmitField('Get Top Citites')


class CityStateSearchForm(FlaskForm):
    state = StringField('State Abbrev.', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Get Rates')
