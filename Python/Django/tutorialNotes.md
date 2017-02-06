# Django Notes

Notes on the tutorial found [here](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)

## Getting started:
Installing:
```
sudo pip install django
sudo pip3 install django
```

Creating a project:

Initial setup will auto-generate some code that will take care of settings and configurations for the Django project

```
$ django-admin startproject mysite
```
This will create a **mysite** directory in your current directory.

> Traditionally PHP and other code is put under the Web servers document root `/var/www`. We don't do that in Django. Other dirs are fine, such as `/home/mycode`

Here's what **startproject** created:
```
mysite/
	manage.py
	mysite/
		__init__.py
		settings.py
		urls.py
		wsgi.py
```
These files are:
- outer **mysite/** - just a container for your poject. Its name doesn't matter to Django. You can rename it to anything.
- **manage.py** - A command-line utility that lets you interact with this Django project in various ways. [Docs](https://docs.djangoproject.com/en/1.10/ref/django-admin/)
- inner **mysite/** - the actual python package for your project. Its name is the package name you'' need to use to import anything e.g. `mysite.urls`
- **mysite/__init__.py** - An emppty file that tells {ython that this directory should be considered a Python package.
- **mysite/settings.py** - Settings/configurations for this Django project. [Docs](https://docs.djangoproject.com/en/1.10/topics/settings/)
- **mysite/urls.py** - The URL declarations for this Django project; a "table of contents" of your Django-powered site. [Docs](https://docs.djangoproject.com/en/1.10/topics/http/urls/)
- **mysite/wsgq.py** - An entry-point for WSGI-compatible webservers to serve your project. [Docs](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/)

### Development server
To verify that your Django project works, from the outer **mysite** dir run:
```
$ python manage.py runserver
```

This launches the Django development server, a lightweight Web server wwritten purely in Python.
By default the `runserver` command starts the development server on the internal IP at port 8000.
If you want to change the server's port, pass it as a command-line argument. For instance, this command starts the server on port 8080:
```
$ python manage.py runserver 8080
```
If you want to change the server's IP, pass it along with the port. So to listen on all public IPs(useful f you want to show off your work on other computers on your network), use:
```
$ python manage.py runserver 0.0.0.0:8080
```
[Docs](https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-runserver)

---

## Creating the Polls app (example)

> **Projects vs Apps**
> What's the difference between a project and an app? An app is a web application that does something. A project is a collection of configuration and apps for a particular website.

To create your app in the same dir as **manage.py** use:
```
$ python manage.py startapp polls
```
This creates a directory **polls**, which is laid out like this:
```
polls/
	__init__.py
	admin.py
	apps.py
	migrations/
		__init__.py
	models.py
	tests.py
	views.py
```
## Write your first view
In the polls/views.py file write:
```python
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
```

This is the simplest view possible in Djang. To call the view, we need to map it to a URL - and for this we need a URLconf. To create a URLconf in the polls directory, create a file called urls.py. Your app dir should look like this:
```
polls/
	__init__.py
	admin.py
	apps.py
	migrations/
		__init__.py
	models.py
	tests.py
	urls.py
	views.py
```

Write this in polls/urls.py:
```python
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
```
The next step is to point the root URLconf at the **polls.urls** module. In the **mysite/urls.py**, add an import for **django.conf.urls.include**
