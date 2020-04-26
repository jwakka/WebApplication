from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, validators, TextAreaField,ValidationError
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):

    name = TextField("Nombre",  [validators.Required("Please enter your name.")])
    email = TextField("Correo Electrónico",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Asunto",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Mensaje",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Enviar")
 