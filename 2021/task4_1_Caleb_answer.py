import flask, sqlite3

app = flask.Flask(__name__)

def get_db():
    db = sqlite3.connect("Task4.db")
    return db


@app.route("/")
def home():
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
