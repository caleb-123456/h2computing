#Task 4.4
import flask, sqlite3

app = flask.Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect("LIBRARY.db")
    cursor = db.cursor()
    
    cursor.execute("""
                SELECT Member.FamilyName, Member.GivenName, Book.Title
                FROM Member
                JOIN Loan
                ON Member.MemberNumber = Loan.MemberNumber
                JOIN Book
                ON Loan.BookID = Book.BookID
                WHERE Loan.Returned = 'FALSE'
                """)
    results = cursor.fetchall()
    
    db.close()
    
    return flask.render_template("index.html", results = results)

app.run(debug = True)
