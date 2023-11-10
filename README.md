# Django-blog-task
Django blog task for Mir Media

## Check the app online
http://179.43.127.129:8000/

## Check the app in localhost
Go in the browser to http://127.0.0.1:8000

## Settings

Project developed with Python 3.11 and Django 4.2.7. Credentials and config are stored in a .env file, and dependencies are listed in the requirements.txt.

- Check you have a .env file with Environment Variables like this:

```dotenv
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
RECIPIENT = 
```

**Apply migrations**\
```python .\manage.py migrate```

**Run the app**\
```python .\manage.py runserver```

**Run tests**\
```python .\manage.py test apps```


## In case of using docker

```
# Build Docker image
docker build -t django-blog .

# Run Docker container
docker run --name django-blog -p 80:80 django-blog
docker run --name django-blog -p 80:80 -v .:/app django-blog

# Run like test
docker build -f Dockerfile.dev -t django-blog-test .
docker run -d --name django-blog -p 80:8000 -v .:/app django-blog-test
docker start django-blog
docker logs -f django-blog

# When you update the image
docker build -f Dockerfile.dev -t django-blog-test .
docker kill django-blog
docker rm django-blog
docker run -d --name django-blog -p 80:8000 -v .:/app django-blog-test

```


