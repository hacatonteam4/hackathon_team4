# MVP Career Tracker

## Описание проекта

Сервис предназначен для создания индивидуального плана обучения пользователя на основе навыков, которые ему нужно развить и курсов Яндекс Практикума, которые обеспечат это развитие.


## Локальный запуск приложения в Docker  

Склонировать репозиторий на свой компьютер и перейти в корневую папку:
```python
git clone git@github.com:hacatonteam4/hackathon_team4.git
cd career_tracker_backend
```

Создать в корневой папке файл .env с переменными окружения, необходимыми
для работы приложения.

Пример содержимого файла:
```
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

SECRET_KEY=key
USE_SQLITE=False
```

Из корневой директории запустить сборку контейнеров с помощью
docker-compose:
```python
docker-compose up -d
```

После этого будут созданы и запущены в фоновом режиме контейнеры
(db, backend, frontend, nginx).
А также база данных наполнится тестовыми данными.

Если что то пошло не так, необходимо сделать следующее:
```python
cd career_tracker_backend
dos2unix run.sh
cd ..
docker-compose up -d
```

После этого проект должен стать доступен по адресу http://localhost:5173/.

Для попадания в админ-зону, перейдите по адресу http://localhost:8000/admin/.

Затем ведите логин и пароль:
- login: admin
- password: admin


### Остановка контейнеров

Для остановки работы приложения можно набрать в терминале команду Ctrl+C
либо открыть второй терминал и воспользоваться командой:
```
docker-compose stop
```

Снова запустить контейнеры без их пересборки можно командой
```
docker-compose start
```


### Спецификация API в формате Redoc:

Чтобы посмотреть спецификацию API в формате Redoc, нужно локально запустить
проект и перейти на страницу http://localhost/api/swagger/ или http://localhost/api/redoc/


## Технологии

* Python 3.9
* Django 3.2
* Django REST framework 3.13
* Nginx
* Docker
* Postgres
