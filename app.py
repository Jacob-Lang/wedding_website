import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
PASSWORD = os.environ.get("PASSWORD")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wedding.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.String(10), nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    song = db.Column(db.String(100))


# Create the database file (Run this once)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            error = "Invalid password. Please try again!"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        # Get data from the form
        new_guest = Guest(
            name=request.form.get("name"),
            attending=request.form.get("attending"),
            meal=request.form.get("meal"),
            song=request.form.get("song"),
        )
        db.session.add(new_guest)
        db.session.commit()
        return "<h1>Thanks for RSVPing!</h1><a href='/'>Back Home</a>"

    return render_template("rsvp.html")


@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    all_guests = Guest.query.all()
    return render_template("admin.html", guests=all_guests)


if __name__ == "__main__":
    app.run(debug=True)
