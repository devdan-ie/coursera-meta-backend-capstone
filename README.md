Make sure to edit settings.py to point to your mysql instance.

Install dependencies with pip/venv
```
cd coursera-backend-capstone
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

OR install dependencies with pipenv
```
pipenv shell
```

Then run
```
cd littlelemon
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

You can also run tests with:
```
python manage.py test
```


How to see the static files:
http://localhost:8000/restaurant

How to access admin portal
http://localhost:8000/admin/


There is a postman collection v2 you can import to guide your testing.

Auth
GET http://localhost:8000/auth/users/
POST http://localhost:8000/api-token-auth/

Menu Items
GET http://localhost:8000/restaurant/menu
POST http://localhost:8000/restaurant/menu

GET http://localhost:8000/restaurant/menu/2
PUT http://localhost:8000/restaurant/menu/1
DELETE http://localhost:8000/restaurant/menu/1


Booking (all end with slash)
GET http://localhost:8000/restaurant/booking/tables/
POST http://localhost:8000/restaurant/booking/tables/

GET http://localhost:8000/restaurant/booking/tables/2/
PUT http://localhost:8000/restaurant/booking/tables/1/
DELETE http://localhost:8000/restaurant/booking/tables/1/

