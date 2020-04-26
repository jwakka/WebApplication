from flask import Flask, render_template, url_for, redirect, request, flash
from form import ContactForm
from flask_mail import Mail, Message
import os

mail  = Mail()


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_USE_TLS'] = False
app.config["MAIL_USERNAME"] = 'juanhuaca91@gmail.com'
app.config["MAIL_PASSWORD"] = 'zhzrqrfpdwbrkxvi'


mail.init_app(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html' ,  title = 'About')

@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('contactUs.html', form=form)
        else:
            msg = Message(form.subject.data, sender='juanhuaca91@gmail.com', recipients=['ecabogadosjm@gmail.com'])
            msg.body= """
            From: %s &;%s&gt;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
 
            return render_template('contactUs.html', success=True)
    elif request.method == 'GET':
        return render_template('contactUs.html', form = form)


