Проект "моей библиотека" на Django


Формы "добавить книгу", "добавить автора" и "добавить друга" реализованы с помощью django-crispy-forms и находятся на странице списка книг, авторов и друзей, соответственно.


Деплой на Heroku при помощи модуля django-heroku

Далее, для добавления таблиц и содержимого базы данных:

heroku run python manage.py makemigrations p_library

heroku run python manage.py migrate

heroku run python manage.py loaddata data.json


Сайт библиотеки на Heroku: https://tortlibrary.herokuapp.com/
