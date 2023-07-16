# Receipt Service

## Installation

1. Clone the repository:
```shell
git clone https://github.com/ostapT/receipt_service.git
```
2. Set up a virtual environment:
```shell
python -m venv venv
source venv/bin/activate (on MacOS/Linux)
venv\Scripts\activate (on Windows)
```
3. Fill .env file using .env.sample like an example.
4. Install required dependencies
```shell
pip install requirements.txt
```
5. Start the required services (redis, postgresql, wkhtmltopdf) using Docker Compose:
```shell
docker-compose up
```
6. Run Celery to handle asynchronous tasks:
```shell
celery -A receipt_service worker --loglevel=info
```

7. Apply database migrations:
```shell
python manage.py makemigrations
python manage.py migrate
```
8. Load the list of printers from the fixture:
```shell
python manage.py loaddata printers.json
```
9. Create a superuser for accessing the admin panel:
```shell
python manage.py createsuperuser
```
10. Start the development server:
```shell
python manage.py runserver
```

## API Endpoints

- Create Order: POST `/api/create_order/`

Endpoint for creating a new order. Sends a POST request with order data to generate receipts.

Example request:
POST /api/create_order/
Content-Type: application/json
```
{
"point_id": "1",
"order": {
    "order_id": "1101",
    "PASTA": "vegan",
    "BURGER": "with beef"
    }
}
```