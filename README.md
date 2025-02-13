# Это первый проект для фриланс заказа

## Описание:
Это сайт для большой дружной семьи, чтобы хранить в виде базы данных информацию о всех членах семьи.

## Развертка проекта на локальном сервере:
<p>
Развертка происходит за счет средств Django и XAMPP <br />
Для начала запустите сервер MySQL в XAMPP и создайте таблицу с названием family <br />
Далее выполните команды в терминале
</p>

```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py collectstatic
  python manage.py createsuperuser
  python manage.py runserver
```
Далее переходите по ссылке в консоли
## Технологии и версии:
<p>
  Python == 3.10 <br />
  Остальные модули и версии есть в requirements.txt
</p>

