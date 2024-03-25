# A Paint Company Backend

## Running Locally

1. Clone the repository, then navigate to the project folder.

2. Create a virtual environment and activate it.

```bash
python3 -m venv env

# On MacOS or Linux
source env/bin/activate

# On Windows
env\Scripts\activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server. The API should now be accessible at `localhost:8000`

```bash
python manage.py runserver
```
