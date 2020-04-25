"""
Project: Halbur's Custom Guns
By: Michaela Rose Roberts
"""


from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def experience():
    return render_template('experience.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
