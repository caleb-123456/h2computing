import flask
import sqlite3

app = flask.Flask(__name__)


def get_db():
    db = sqlite3.connect("Task4.db")
    return db


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/round1")
def round1():

    db = get_db()

    data = db.execute("""
        SELECT competitor.name, scores.score
        FROM competitor
        INNER JOIN scores
        ON competitor.id = scores.id
        WHERE scores.round = 1
        ORDER BY scores.score DESC
    """).fetchall()

    db.close()

    return flask.render_template("round.html", data=data, round=1)


@app.route("/round2")
def round2():

    db = get_db()

    data = db.execute("""
        SELECT competitor.name, scores.score
        FROM competitor
        INNER JOIN scores
        ON competitor.id = scores.id
        WHERE scores.round = 2
        ORDER BY scores.score DESC
    """).fetchall()

    db.close()

    return flask.render_template("round.html", data=data, round=2)


@app.route("/round3")
def round3():

    db = get_db()

    data = db.execute("""
        SELECT competitor.name, scores.score
        FROM competitor
        INNER JOIN scores
        ON competitor.id = scores.id
        WHERE scores.round = 3
        ORDER BY scores.score DESC
    """).fetchall()

    db.close()

    return flask.render_template("round.html", data=data, round=3)


@app.route("/mean")
def mean():

    db = get_db()

    data = db.execute("""
        SELECT competitor.name, ROUND(AVG(scores.score), 2)
        FROM competitor
        INNER JOIN scores
        ON competitor.id = scores.id
        GROUP BY competitor.id, competitor.name
        ORDER BY competitor.name ASC
    """).fetchall()

    db.close()

    return flask.render_template("mean.html", data=data)


@app.route("/qualifiers")
def qualifiers():

    db = get_db()

    data = db.execute("""
        SELECT competitor.name,
               SUM(scores.score),
               CASE
                   WHEN SUM(scores.score) > 250 THEN 'Qualified'
                   ELSE 'Not Qualified'
               END
        FROM competitor
        INNER JOIN scores
        ON competitor.id = scores.id
        GROUP BY competitor.id, competitor.name
        ORDER BY SUM(scores.score) DESC
    """).fetchall()

    db.close()

    return flask.render_template("qualifiers.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)


