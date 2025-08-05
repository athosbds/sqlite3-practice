from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'requestsmethods@#$'

class ContatoForm(FlaskForm):
    nome = StringField('Seu nome', validators=[DataRequired()])
    mensagem = TextAreaField('Sua mensagem', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

@app.route('/')
def home():
    return redirect(url_for('contato'))
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    enviado = False
    if form.validate_on_submit():
        enviado = True
        return render_template('contact.html', form=form, enviado=enviado)
    return render_template('contact.html', form=form, enviado=enviado)


if __name__ == '__main__':
    app.run(debug=True)