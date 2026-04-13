import os
import json
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session
import csv
import io
from flask import make_response

load_dotenv()

with open("wedding_config.json") as f:
    WEDDING_CONFIG = json.load(f)

app = Flask(__name__)


@app.context_processor
def inject_wedding_config():
    return {"wedding": WEDDING_CONFIG}


app.secret_key = os.environ.get("SECRET_KEY")
PASSWORD = os.environ.get("PASSWORD")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getenv('DATABASE_URL')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.String(10), nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    dietary_requirements = db.Column(db.String(100))


# Create the database file (Run this once)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/details")
def details():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("details.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            error = "Invalid password. Please try again!"
    return render_template("login.html", error=error, admin_mode=False)


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        if request.form["password"] == ADMIN_PASSWORD:
            session["logged_in"] = True
            session["is_admin"] = True
            return redirect(url_for("home"))
        else:
            error = "Invalid password. Please try again!"
    return render_template("login.html", error=error, admin_mode=True)


@app.route("/logout")
def logout():
    session.clear()
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
            dietary_requirements=request.form.get("dietary_requirements"),
        )
        db.session.add(new_guest)
        db.session.commit()
        return "<h1>Thanks for RSVPing!</h1><a href='/'>Back Home</a>"

    return render_template("rsvp.html")


@app.route("/admin")
def admin():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    all_guests = Guest.query.all()
    return render_template("admin.html", guests=all_guests)


@app.route("/admin/export")
def export_csv():
    # 1. Security check - only admins can export!
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    # 2. Get the data
    guests = Guest.query.all()

    # 3. Create an "in-memory" file
    output = io.StringIO()
    writer = csv.writer(output)

    # 4. Write the header row
    writer.writerow(["Name", "Attending", "Meal", "Song Request"])

    # 5. Write the data rows
    for guest in guests:
        writer.writerow([guest.name, guest.attending, guest.meal, guest.song])

    # 6. Create the response
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=wedding_rsvps.csv"
    response.headers["Content-type"] = "text/csv"

    return response


if __name__ == "__main__":
    app.run(debug=True)
