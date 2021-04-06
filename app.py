from flask import Flask, render_template, jsonify, request

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kibana")
def kibana():
    return render_template("kibana.html")

if __name__ == "__main__":
    app.run()