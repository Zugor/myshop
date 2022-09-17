````
#Install django lib
pip3 install django

#Create django project
django-admin startproject project_name

#Create a App in the project
python manage.py startapp app_name

#Run server to access your website http://127.0.0.1:8000
python manage.py runserver

#Apply changes of a model
python manage.py makemigrations app_name
python manage.py migrate

#Create super user to login Admin page
python manage.py createsuperuser
````
