from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods = ['POST'])
def submit():
    return "<h1>Welcome to our webpage," + request.form['fullName']  + "</h1>" 

if __name__ == "__main__":
    app.run()