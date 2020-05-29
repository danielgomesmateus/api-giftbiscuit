# api-giftbiscuit

1) Requisitos para o projeto:

- asgiref==3.2.5
- boto3==1.12.41
- certifi==2019.11.28
- chardet==3.0.4
- Django==3.0.4
- django-cors-headers==3.2.1
- djangorestframework==3.11.0
- djangorestframework-jwt==1.11.0
- django-storages==1.9.1
- drf-yasg==1.17.1
- gunicorn==20.0.4
- idna==2.9
- jsonpath==0.82
- mysqlclient==1.4.6
- Pillow==7.0.0
- psycopg2-binary==2.8.5
- pytz==2019.3
- requests==2.23.0
- six==1.14.0
- sqlparse==0.3.1
- urllib3==1.25.8

2) Crie dois arquivo com o nome ".env.dev" e ".env.prod" e adicione o conteúdo abaixo:

```
DEBUG=
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=

SQL_ENGINE=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=
SQL_PORT=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=

AWS_STORAGE_BUCKET_NAME=
AWS_DEFAULT_ACL=
AWS_S3_REGION_NAME=

AWS_LOCATION=
AWS_QUERYSTRING_AUTH=
```

Complete com as informações relativas ao seu ambiente.

3) Para iniciar o projeto, utilize o comando abaixo:

```
docker-compose up -d --build
```

4) Com a imagem gerada e os serviços ativos, execute o comando abaixo dentro do container web:

```
python3 manage.py migrate
```

5) Execute o comando abaixo dentro do container web para definir o seu usuário administrador:

```
python3 manage.py createsuperuser
```

6) Para visualizar o projeto, acesse o endereço abaixo:

```
http://localhost:8082/v1/
```

7) Para visualizar a documentação da API, acesse o endereço abaixo:

```
http://localhost:8082/v1/docs
```