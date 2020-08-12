from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError, validators
from flask_wtf.file import FileField,FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    login = SubmitField('Log In')
    register = SubmitField('Register')

class SearchForm(FlaskForm):
    option = StringField('', validators=[DataRequired(),Length(max=40)], render_kw={"placeholder": "Search Item"})
    quantity = StringField('', validators=[DataRequired(),Length(max=40)], render_kw={"placeholder": "Quantity"})
    update = SubmitField('Synch')
