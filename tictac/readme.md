This project is a simple crud app that builds the foundation
for a tic-tac-toe like game.

### How to run

```commandline
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
Install djangorestframework

```commandline
# Install Django and Django REST framework into the virtual environment

pip install djangorestframework
```

Create a migration, this will create the code required to add new database table for Item model:

```commandline
python manage.py makemigrations
```

Run migrate command to perform database operation (if that’s the first time you run this command, it will also apply default Django migrations, for creating tables etc.)

```commandline
python manage.py migrate
```

Run the app

```commandline
python manage.py runserver
```

* Project took about 2-3 hours.
* Mainly focused on the api framework and design
* Main logic/validation for the game itself was not complete, due to time constraints.
* Ideally we should have player model too
* I like the approach of this interview, the freedom and flexibility to use any tech is good. Tho I think 2-3 hour for full set of APIs + testing + validations is kind of a lot.
* 