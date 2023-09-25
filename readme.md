## Запуск приложения

скачать файлы из репозитория
```
git clone https://github.com/alex-s2222/upload_file_task.git
```

Перейти в папку проекта
```
cd upload_file_task
```

создать сервис
```
docker compose build 
```

запустить сервис
```
docker compose up
```

запустить миграцию в базе данных
```
docker exec my-django-app python mysite/manage.py migrate --noinput
```

## Возможные ошибки

сначало создается django app после него уже база данных, если такое произошло, нужно перезапустить django контейнейнер (в docker-compose.yaml указал, что бы сначало собирался postgres контейнер) (в чем ошибка не знаю)
```
docker restart my-django-app
```
