from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=40)])
    phone_number = StringField('phone_number', validators=[DataRequired(), Length(min=8, max=11)])
