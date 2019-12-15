from flask import Flask, render_template, request
app = Flask(__name__)
import os

from core import register_user

@app.route('/')
def hello_world():
    return render_template('landing.html')

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/register/', methods=['POST'])
def register():
    personal_token, share_token = register_user(request.form['name'],
                                                request.form['button_number'],
                                                request.form['contacts'])
    return render_template('token.html',
                           personal_token=personal_token,
                           share_token=share_token)

if __name__ == '__main__':
    if 'hansel_dev' in os.environ:
        app.run()
    else:
        app.run(host='0.0.0.0', port=80)

