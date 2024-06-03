python manage.py (prees enter for all command list)
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

1-Venv:
	Py -m venv venv
	Venv\Scripts\activate
2-requirements:
	pip freeze > requirements/base.txt
	pip freeze > requirements.txt
	pip install -r requirements.txt
	pip install -r requirements/base.txt
	curl -o requirements.txt curl -o base.txt (Git Hub Raw)
	raw
	pip install -r requirements.txt or requirements/base.txt

3-Project:
	New:
		pip install django
		pip install djangorestframework
		pip install markdown
		pip install django-filter
		pip install psycopg2-binary
		pip install gunicorn
		pip install django-environ
		Or (specific copy [such as this copy at the time)
		pip install django==5.0.6
		pip install djangorestframework==3.15.1
		pip install markdown==3.6
		pip install django-filter==24.2
		pip install django-environ==0.11.2
		pip install psycopg2-binary==2.9.9
		pip install gunicorn==22.0.0
		Or 
		pip install -r requirements.txt
		pip install -r requirements/base.txt

	Exists:
		curl -o base.txt (Git Hub Raw)
		raw
		pip install -r requirements.txt or requirements/base.txt

4-Command Prompt : 
	# لتشغيل البيئة التطويرية
	set DJANGO_SETTINGS_MODULE=yourName.settings.development

	# لتشغيل البيئة الإنتاجية
	set DJANGO_SETTINGS_MODULE=yourName.settings.production

	# لتشغيل البيئة الاختبارية
	set DJANGO_SETTINGS_MODULE=yourName.settings.testing

	# لتشغيل بيئة التدريج
	set DJANGO_SETTINGS_MODULE=yourName.settings.staging

	# ثم قم بتشغيل الخادم
	python manage.py runserver
	or
	set DJANGO_ENV=development
	python manage.py runserver

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[rest_framework]
    generateschema

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

