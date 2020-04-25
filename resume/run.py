from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/biography')
def about_me():
    return render_template("about_me.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')