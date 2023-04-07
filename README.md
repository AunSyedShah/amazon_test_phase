# Amazon Seller central Test Phase
### How to run the project
#### run these commands in the terminal
##### Option 1 - With Virtual Environment
```commandline
python -m pip install virtualenv
python -m virtualenv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations main_app
python manage.py migrate
python manage.py runserver
```
##### Option 2 - Without Virtual Environment
```commandline
pip install -r requirements.txt
python manage.py makemigrations main_app
python manage.py migrate
python manage.py runserver
```

##### How to create superuser
```commandline
python manage.py createsuperuser
```