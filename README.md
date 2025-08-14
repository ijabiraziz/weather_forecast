Create Virtual Environment & Activate
python -m venv venv
venv\Scripts\activate # Windows
or
source venv/bin/activate # macOS/Linux

Install Dependencies
pip install -r requirements.txt

Database Configuration

Open pgAdmin (or your PostgreSQL client).

Create a new database with the name you will use in config.json.

At the root directory of the project, add a file named config.json with:

{
"DB_NAME": "db-namee",
"DB_USER": "ps-user-name",
"DB_PASSWORD": "yourpassword",
"DB_HOST": "localhost",
"DB_PORT": "5432"
}



Run Migrations
python manage.py makemigrations
python manage.py migrate

Start Server
python manage.py runserver

Frontend Endpoints (Django Templates - Jinja)
Login: http://127.0.0.1:8000/accounts/login
Signup: http://127.0.0.1:8000/accounts/signup
Predictions Form: http://127.0.0.1:8000/predictions/

Notes

Uses Django's default templating engine (Jinja-like syntax).

Make sure PostgreSQL is running before starting the server.

All prediction requests are stored in the database per user.
