# api-giftbiscuit

1) Requisitos para o projeto:

- asgiref==3.2.5
- boto3==1.12.41
- certifi==2019.11.28
- chardet==3.0.4
- Django==3.0.4
- djangorestframework==3.11.0
- djangorestframework-jwt==1.11.0
- django-storages==1.9.1
- drf-yasg==1.17.1
- idna==2.9
- jsonpath==0.82
- mysqlclient==1.4.6
- Pillow==7.0.0
- pytz==2019.3
- requests==2.23.0
- six==1.14.0
- sqlparse==0.3.1
- urllib3==1.25.8

2) Utilize o comando abaixo para subir um banco de dados MySQL via Docker:

```
docker-compose up
```

Obs.: O dump do banco está na pasta utils/DB

3) Crie um arquivo com o nome "local_settings.py" e adicione o conteúdo abaixo:

```
from .settings import *

SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 3306
    }
}

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

AWS_STORAGE_BUCKET_NAME = ''
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = ''
AWS_S3_REGION_NAME = ''

AWS_LOCATION = ''
AWS_QUERYSTRING_AUTH = ''

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

DEFAULT_FILE_STORAGE = 'apigiftbiscuit.storage_backends.MediaStorage'
```

Complete com as informações relativas ao seu ambiente.

4) Com a conexão ao banco realizada, execute o comando abaixo:

```
python3 manage.py migrate --settings=apigiftbiscuit.local_settings
```

5) Execute o comando abaixo para definir o seu usuário administrador:

```
python3 manage.py createsuperuser --settings=apigiftbiscuit.local_settings
```

6) Para iniciar o projeto, utilize o comando abaixo:

```
python3 manage.py runserver --settings=apigiftbiscuit.local_settings
```

7) Para visualizar a documentação da API, acesse o endereço abaixo:

```
http://localhost:8000/v1/docs
```