# justworktest

Проект являет собой тестовое задание, представлен в качестве примера. 

## Базовая архитектура

* Docker 18.09
* Docker-compose 1.17
* Pipenv 18.11
* Python 3.7
* Django 2.2
* Celery 4.3
* Redis 3.2 + Redis server 4.0 
* PostgreSQL (latest) + psycopg2-binary 2.7
* Django Rest Framework 3.9
* Swagger 2.2
* и т.д. ... 

Все зависимости прописаны в фаилах Pipfile и Pipfile.lock

## Cборка и запуск

Выполняем сборку приложения
```
$ docker-compose up
```
Выполняем миграции
```
$ docker-compose run cli migrate
```
Создаём суперпользователя
```
$ docker-compose run cli createsuperuser
```
Открываем браузер по адресу http://0.0.0.0:8000

## Фикстуры и тесты

...

## API v1

Метод GET - получить информацию о всех страницах (для пагинации задаються параметры limit и offset)
```
http://localhost:8000/api/v1/pages/
```

Пример запрос c параметрами limit и offset
```
Request url: http://0.0.0.0:8000/api/v1/pages/?limit=1&offset=2

Request command: curl -X GET "http://0.0.0.0:8000/api/v1/pages/?limit=1&offset=2" -H "accept: application/json" -H "X-CSRFToken: JWmaO9NKcgAlzE6Dbd2KiOjBMaXhhVzTk8x67GrcPTHfc0cO7vUuVeu4oQIScjd4"
```

Пример ответа
```
{
  "count": 3,
  "next": null,
  "previous": "http://0.0.0.0:8000/api/v1/pages/?limit=1&offset=1",
  "results": [
    {
      "url": "http://0.0.0.0:8000/api/v1/page/3/"
    }
  ]
}
```

Метод GET - получить детальную информацию о странице с {id}
```
http://localhost:8000/api/v1/page/{id}/
```
Пример запроса
```
Request url: http://127.0.0.1:8000/api/v1/page/1/
Request command: curl -X GET "http://0.0.0.0:8000/api/v1/page/1/" -H "accept: application/json" -H "X-CSRFToken: JWmaO9NKcgAlzE6Dbd2KiOjBMaXhhVzTk8x67GrcPTHfc0cO7vUuVeu4oQIScjd4"
```
Пример ответа:
```
{
  "id": 1,
  "audio": [
    {
      "id": 1,
      "title": "Аудиозапись №1",
      "order": 10,
      "counter": 2,
      "bitrate": 16,
      "page": 1
    }
  ],
  "video": [
    {
      "id": 1,
      "title": "Тестовое видео №1",
      "order": 10,
      "counter": 2,
      "video": "/uploads/media/video/2019/04/03/video.mkv",
      "subtitles": "/uploads/media/video/2019/04/03/subtitles.txt",
      "page": 1
    }
  ],
  "text": [
    {
      "id": 1,
      "title": "Текстовая запись №1",
      "order": 10,
      "counter": 2,
      "text": "Контент",
      "page": 1
    }
  ],
  "title": "Тестовая страница №1",
  "order": 10,
  "counter": 0,
  "slug": "testovaya-stranica-1"
}
```

## Примечания

* Сортировка всех сущностей осуществляется по полю 'order'
* После просмотра каждой сущности поле 'counter' увеличивается на 1 ед. в асинхронном и атамарном порядке, посредством Celery
* Поиск в админке работает по всем поляем, в т.ч. по всем основным полям в связанных моделях
* Для отслеживания результата работы воркеров см. ./justwork/worker.log