# Adverts Listing

**Adverts Listing** is a simple web application that allows you to create your ad listing.

# Deployment process

## 1. Set environment variables
Default values are set in the docker-compose.yml file. 
To overwrite it, create .env file in a root folder with the following contents:

```bash
    DEBUG=True/False
    DB_NAME=db_name
    DB_USER=db_user
    DB_PASS=db_pass
    DB_HOST=db_host
    DB_PORT=5432
    SECRET_KEY=django_secret_key
    ALLOWED_HOSTS=*
```

## 2. Run commands

```bash
    docker-compose up -d --build
    docker-compose exec web python3 manage.py createsuperuser --username admin
```

## 3. Configure the app

**Access admin panel**

In order to access admin settings, follow the `<your-domain>.com/admin` URL and sign in
using the superuser credentials.
