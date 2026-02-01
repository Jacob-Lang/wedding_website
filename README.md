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

http://localhost:8000
