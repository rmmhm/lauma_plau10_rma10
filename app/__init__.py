from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("data.db")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)")
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("0", "voldy", "darklord"))
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("1", "harry", "chosen"))
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("2", "fred", "bettertwin"))
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("3", "george", "besttwin"))
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("4", "hermoine", "iamsmrt"))
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("5", "ron", "hermoine"))
db.commit()

@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("slides.html")

@app.route("/injection", methods=["POST"])
def injection():
    return render_template("injection.html")

@app.route("/injection1", methods=["POST"])
def injection1():
    db = sqlite3.connect("data.db")
    c = db.cursor()
    select = "SELECT * from users WHERE userID = " + request.form["badUserID"]
    data = c.execute(select)
    return render_template("injection.html", data=data)

@app.route("/injection2", methods=["POST"])
def injection2():
    db = sqlite3.connect("data.db")
    c = db.cursor()
    select = 'SELECT * from users WHERE username = "' + request.form["badUsername"] + '"'
    data = c.execute(select)
    return render_template("injection.html", data=data)

@app.route("/userID", methods=["POST"])
def userID():
    db = sqlite3.connect("data.db")
    c = db.cursor()
    data = c.execute("SELECT * from users WHERE userID=?", (request.form["userID"],))
    return render_template("injection.html", data=data)

@app.route("/username", methods=["POST"])
def username():
    db = sqlite3.connect("data.db")
    c = db.cursor()
    data = c.execute("SELECT * from users WHERE username=?", (request.form["username"],))
    return render_template("injection.html", data=data)

if(__name__ == "__main__"):
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
    db.close()