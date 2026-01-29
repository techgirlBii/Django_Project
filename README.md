# Django
Django is a back-end server side web framework. It is free, open source and written in Python. Django is a Python framework that makes it easier to create web sites using Python. It takes care of the difficult stuff so that you can concentrate on building your web applications.

Django emphasizes reusability of components, also referred to as  DRY (Don't Repeat Yourself),
and comes with ready-to-use features like login system, database connection and
CRUD operations (Create Read Update Delete).
Django is especially helpful for database driven websites.


**Django follows the MVT design pattern (Model View Template).**

**Model** - The data you want to present, usually data from a database.

**View** - A request handler that returns the relevant template and content - based on the request from the user.

**Template** - A text file (like an HTML file) containing the layout of the web page,
 with logic on how to display the data.

## What is a Model? 
 A Model provides data from the databases. That is data used for building the application.
 In Django, the data is delivered as an **Object Relational Mapping (ORM)**, 
 which is a technique designed to make it easier to work with databases,
 One of the common ways we can extract data is using SQL  but the thing is, if you dont
 have basic undertanding of how that works, its diffcult. So Django uses ORM to make it easier for you.
 The models/ data is located in a file called models.py

 
 
## What are Views?
Views  are Python functions that take http requests and return http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

## What is a Template?
Templates are folders that contain html documents to be rendered on the front end.

## What are URL'S ?
Urls in django are files containing path functions that tells the views where to go and what to display.


### Use the following commands to start a Django Project:
After confirming you have python and pip installed 

Create a virtual env using the command :
```
 python -m venv the_name_of_your_virtual_env
 ```

Then activate it  using : 
```
cd myvenv , cd Scripts , activate
```

Now Install Django using :
``` 
python -m pip install Django
```
Now start your first project using : 
```
django-admin startproject the_name_of your_project
```
**Run your project always using :**
```
python manage.py runserver
```
Now create an app in Django using :
```
python manage.py startapp name_of_your_app
```


## CREATING TABLES IN MODELS
Go  to the models.py file on your app and add a class_name with its attributes :
```
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

```
Now run this command to create the table in the database:
```
python manage.py makemigrations name_of_app
```
After it run you can check it in the migrations.py file in your app then run :
```
python manage.py migrate
```

You can view your model data as an sql statements:
```
python manage.py sqlmigrate members 0001
```

** A QuerySet is a collection of data from a database ** 

### To add records or data to your table use:
Go to shell :
```
python manage.py shell
```

Then add data using :
```
from app_name.models import class_name_in_the_model

i.e from members.models import Member
```
Now  add  values :
```
member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()
```

### To see the values you have added use :
```
 Theclassname.objects.all().values
  e.g Member.objects.all().values()
 ```

Now to add other values to the table :

```
y = Member(name, lastname etc)
```
Then save:
```
y.save()
```
You can add other items in that same table using:
```
y1 = Member(name, lastname etc)
y2 = Member(name,lastname etc) ...
```

###  *Note: Before adding other attributes to your existing data in your models, make sure to set those attributes to null else it will throw an error* .

## Displaying data on templates
You can display data on the following : 

* Any html file e.g details.html , new.html
* Base template/Master template e.g base.html used as the main html structure that other pages inherits from
* Index/Main page - the initially page that is being displayed on the browser
* 404 html page - to display custom error messages after debug has been turned off.
* Test view page - used for testing withiut affecting the main project.

### *Always remeber to add views and urls to the above so allow them to be rendered*

##  Creating a Django Admin Profile
Instead of adding values to the models using only the terminal, you can use the admin profile to add, view, edit and delete users or data. 

Create a user, go to the terminal :
```
python manage.py createsuperuser
```
Fill in the prompts and create user successfully

Run your server and go the admin/ url and log in , you will now see an interface for your models so you can perform CRUD operations.

To register your models so it is visible on the interface, go to admin.py in your app and register your models using:
```
from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(name_of_your_class_name)
i.e admin.site.register(Member)
```






