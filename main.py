from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, EmailField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


class MyForm(FlaskForm):
    email = EmailField('email',
                       [validators.Length(min=6, max=20), validators.data_required(), validators.InputRequired(),
                        validators.Email()])
    password = PasswordField('password', [validators.Length(min=6, max=20), validators.data_required()])
    submit = SubmitField('submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit() and request.method == 'POST':
        usermail = form.email.data
        password = form.password.data
        print(usermail)
        if usermail == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
