## Базовый API интерфейс для BLOG
- CRUD на посты
- Регистрация с активацией, авторизация пользователей
- Комментарии, лайки
 ### Технологии:
> - Django
> - Django Rest Framework
> - Postgresql

### Запуск проекта на локальной машине

## 1.Клонирование репозитория
`git clone https://github.com/racsa5555/blog_2.git`

## 2. Установка необходимых зависимостей
`pip install -r requirements.txt`
Или с poetry
`poetry add $(cat requirements.txt)`

## 3.Создание файла .env

Создайте файл .env 

Пример:
DB_NAME=...
DB_USER=...
DB_PASS=...

SECRET_KEY=...
DEBUG=...

## 5. Запуск проекта
`python3 manage.py runserver`


