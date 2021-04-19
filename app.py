from flask import Flask, render_template, request
from DataPersistence import db

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kibana", methods=['GET'])
def kibana():
    id_token = request.args.get('id_token',None)
    if id_token:
        return render_template("kibana.html")
    else:
       return render_template("index.html")


if __name__ == "__main__":
    conn = db.get_db()
    db.test_connection(conn)
    app.run()

