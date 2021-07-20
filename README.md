[![build and deploy](https://github.com/DRAGANmik/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)](https://github.com/DRAGANmik/yamdb_final/actions/workflows/yamdb_workflow.yaml)
[![pep8 codestyle](https://github.com/DRAGANmik/yamdb_final/actions/workflows/codestyle.yml/badge.svg)](https://github.com/DRAGANmik/yamdb_final/actions/workflows/codestyle.yml)

# api_yamdb

Бэкенд для проекта YaMDb. Сервис для оценивая фильмов, музыки и книг.
Адрес: 84.252.141.179

## Команда разработки:
* Драган Михаил
* Софья Клочко
* Александр Трайнич


## Технологии
```
Python 3.7+
Django
Django REST Framework
Docker
Black - форматирование кода
```

## Установка локально с БД в Docker
- Запустите контейнер с БД:
    ```shell
    docker-compose -f local.yaml up --build -d
    ```
  При первом запуске необходимо применить миграции:
    ```shell
    python manage.py migrate
    ```
  Создать суперпользователя:
    ```shell
    python manage.py createsuperuser
    ```
  
- Теперь можно запустить проект, он будет использовать БД в контейнере:
    ```shell
    python manage.py runserver
    ```
  
- Остановить контейнер с БД:
    ```shell
    docker-compose -f local.yaml down
    ```
- Остановить контейнер с БД удалив данные:
    ```shell
    docker-compose -f local.yaml down --volumes

## Запуск проекта локально в Docker окружении и заполнить данными
- Запустить проект:
    ```shell
    docker-compose up --build -d
     ```
 - Применить миграции:
    ```shell
    docker-compose exec web python manage.py migrate --noinput
    ```
   
- Заполнить базу данных начальными данными из фикстур:
    ```shell
    docker-compose exec web python manage.py loaddata fixtures.json
    ```
- Создать суперпользователя:
  ```shell
  docker-compose exec web python manage.py createsuperuser
    ```
  
- Собрать статику:
  ```shell
    docker-compose exec web python manage.py collectstatic --no-input
    ```
- Запущенный проект доступен по адресу:
    ``http://127.0.0.1``
  
- Админка: ``http://127.0.0.1/admin/ ``


- Остановить проект сохранив данные в БД:
    ```shell
    docker-compose down
    ```
- Остановить проект удалив данные в БД:
    ```shell
    docker-compose down --volumes
    ```

## В проект добавлен Makefile для облегчения запуска management команд

Запуск django сервера c локальными настройками:

```shell
make runserver
```

Создать и применить миграции:
```shell
make migrate
```

Создать суперпользователя:
```shell
make createsuperuser
```
Заполнить базу данных начальными данными из фикстур:
```shell
make fixtures
```

# Запуск тестов
```shell
pytest
```

# Просмотр документации по API
```shell
127.0.0.1:8000/redoc
```
