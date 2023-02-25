# How to run this project
```python
python -m pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```