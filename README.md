# stripe_django_project
Проект, для создания тестовой системы платежей.
Stripe_django_project, позволяет создавать модель товара Item и 
сгенерировать платежную форму при помощи сервиса StripeAPI для оплаты
данного товара.

**Установка проекта**
- Клонирование репозитория:
```bash
git clone git@github.com:AlexandrBuvaev/stripe_django_project.git
cd stripe_django_project/
```
- Создание и активация виртуального окружения:
```bash
Linux:
python3 -m venv venv
source venv/bin/activate
Windows:
python -m venv venv
source venv\Scripts\activate
```
- Установка зависимостей:
```bash
pip install -r requirements.txt
```
- Создание файла .env и добавление переменных окружения:
```bash
cd payments/
/stripe_django_project/payments
...
├── .env
```
- В файл .env добавьте переменные:
```bash
STRIPE_SECRET_KEY = 'your secret key'
STRIPE_PUBLIC_KEY = 'your public key'
```
- Выполнение миграций и запуск локального сервера:
```bash
/stripe_django_project/payments$ python3 manage.py migrate
/stripe_django_project/payments$ python3 manage.py runserver
```
Для корректного запуска так же необходимо через панель админа создать
тестовый товар.
- Создание суперпользователя:
```bash
/stripe_django_project/payments$ python3 manage.py createsuperuser
```
Далее необходимо перейти по адресу: 'http://localhost:8000/admin'
и создать тестовый товар.

Доступные эндпониты:
```bash
http://localhost:8000/item/<item_id>/ - получем карточку товара
http://localhost:8000/buy/<item_id>/ - получаем ссылку на оплату
```
