# Employee Portal

### Follow the Steps to setup this project :

Python Used - 3.7.4

```
$ git clone https://github.com/himdhiman/employee-portal.git
$ cd employee-portal
$ pip install virtualenv
$ virtualenv env
```

Windows Users

```
env\Scripts\activate
```

Mac Users

```
source env/bin/activate
```


```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Go to localhost:8000 on the browser and login as admin with the superuser id.
