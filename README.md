## Setup

To start the project
`uv init --python 3.14`

Dev - reqs
uv, pre-commit, python 3.14, brew install docker-desktop, pip install gunicorn,


Running the website
`uv run python app.py`
Go to localhost link


Query the DB.
As you develop, you might want to see or reset your data. Here is how you "talk" to your database manually in the terminal:
Open your terminal in the project folder.
Type `python` in the shell.
Run these commands:
```
from app import app, db, Guest

with app.app_context():
    # 1. See how many guests are in the DB
    print(Guest.query.count())

    # 2. Delete everyone (if you want to start fresh)
    # Guest.query.delete()
    # db.session.commit()
```


# Docker

build
docker build -t wedding-app .

run
docker run -d -p 8000:8080 \
  --env-file .env.docker \
  -v $(pwd)/instance:/app/data \
  --name wedding-prod wedding-app

-d
By default, when you run docker run, your terminal "attaches" to the container. You see all the logs, and if you close the terminal or press Ctrl + C, the container stops.

Why you use Detached Mode (-d):
When you're running a web server like your wedding site, you want it to behave like a background service.

The Terminal is Freed Up: You get your command prompt back immediately after the container starts.

Independent Life: The container keeps running even if you close the terminal window or log out of your computer.

Background Service: This is the standard way to run databases, web servers, and "always-on" tools.
)


http://localhost:8000
