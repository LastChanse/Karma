@echo off
echo Hosting need ALLOWED_HOSTS = ['name_server', 'www.name_server.com']
echo BUT lochal host already!
cd KarmaMagas
@pause
//py -3.10 manage.py runserver
manage.py runserver
@pause