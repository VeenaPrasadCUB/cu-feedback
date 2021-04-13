from flask import Flask, render_template
import os
import db


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'data')
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kibana")
def kibana():
    return render_template("kibana.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run()



