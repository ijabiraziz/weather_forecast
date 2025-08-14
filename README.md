Create Virtual Environment ( and activate it )
python -m venv venv
venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


add config.json with your PostgreSQL credentials at the root directory:
make sure to first open pgAdmin and create database with the used db name in .json file



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




frontend endpoint (i have used django default templating language (jinja)
http://127.0.0.1:8000/accounts/login
http://127.0.0.1:8000/accounts/signup
http://127.0.0.1:8000/predictions/
