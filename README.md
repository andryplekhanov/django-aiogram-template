# django-aiogram-template

## Setup
```bash
cat .env.dist > .env
# change values in .env

docker-compose build
docker-compose up -d

# to stop
docker-compose down
```

## Database migrations
```bash
# to make new migration files
docker-compose exec web sh -c "python manage.py makemigrations"
# run migrations
docker-compose exec web sh -c "python manage.py migrate"
# create superuser
docker-compose exec web sh -c "python manage.py createsuperuser"
```

## Adminer
Visit http://localhost:8080/ to connect to your database.
- System: PostgreSQL
- Server: db
- Username: postgres
- Password: postgres
- Database: template-db
