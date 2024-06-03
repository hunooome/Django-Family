
Structuring:
Name_Of_Project_Folder_Root
├── apps 
├── build
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   ├── testing.py
│   │   └── staging.py
│   └── envs
│       ├── development.env
│       ├── production.env
│       ├── testing.env
│       └── staging.env
├── doc
├── requirements
├── media
├── static
├── templates
├── venv
├── Project_Name
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── .gitignore


1-General info
	INSTALLED_APPS = [
    		other apps,
    		'rest_framework',
    		'apps.AppName,
	]

	inside apps/app folder/apps.py
	name = ‘apps.AppName’

	env = environ.Env()

	BASE_DIR = Path(__file__).resolve().parent.parent.parent  / 'build' / 'envs' / 	f"{env('DJANGO_ENV', default='development')}.env"
	environ.Env.read_env(BASE_DIR)

	Import os
	'DIRS': ['templates'],

	Ander STATIC_URL
	STATICFILES_DIRS = [
    		os.path.join(BASE_DIR, 'static')
	]



