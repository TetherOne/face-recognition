# Сервис по распознованию лиц

## Функционал
- GET http://127.0.0.1:8015/api/v1/tasks - просмотр списка заданий
- GET http://127.0.0.1:8015/api/v1/tasks/{task_id} - просмотр заданий по id
- CREATE http://127.0.0.1:8015/api/v1/tasks/create - создание задания
- DELETE http://127.0.0.1:8015/api/v1/tasks/{task_id}/delete - удаление задание по id
- CREATE http://127.0.0.1:8015/api/v1/tasks/{task_id}/add-image/ - добавление изображения к заданию, передается название и изображение

## Запуск проекта
#### 1. Клонируйте репозиторий
```
git clone https://github.com/TetherOne/FaceRecognition.git
```
#### 2. Укажите переменные окружения в папке envs
```
- файл app.env
TEVIAN__DB__URL=
TEVIAN__SERVICE__URL=
TEVIAN__SERVICE__TOKEN=

- файл db.env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```
#### 3. В случае, если вы хотите изменять и коммитить изменения проекта - используйте pre-commit
```
pip install pre-commit
pre-commit install
```
#### 4. Соберите проект
```
docker-compose build
docker-compose up
```
В случае ошибки ниже, заменить порты сервисов в docker-compose.yaml, например, с "5430:5432" на "5445:5432"
```
Gracefully stopping... (press Ctrl+C again to force)
Error response from daemon: driver failed programming external connectivity on endpoint
face-recognition-db (e8c24ee790458791d4a3151f4fd8667bd3827f647afe532da66d4748d1f76efd):
listen tcp4 0.0.0.0:5430: bind: address already in use
```
#### 5. Перейдите в браузер по ссылке:
```
http://127.0.0.1:8015/docs
```
