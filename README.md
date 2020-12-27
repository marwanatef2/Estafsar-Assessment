# Estafsar Assessment

This project is a simple web service with a single GET endpoint `/rate`.

This endpoint takes up to 3 query parameters:
- `from` indicates the From Currency.
- `to` indicates the To Currency.
- `date` indicates the date for this rate exchange.
 
## Installation

This project uses [Python](https://www.python.org/downloads/) 3 so if you do not have python running on your machine please download it first.

1. Clone the project.
    ```
    git clone https://github.com/marwanatef2/Estafsar-Assessment.git
    ```
2. Create your own virtual environment.
    ```
    python -m venv venv
    cd venv/Scripts
    . activate
    cd ../..
    ```
3. Install the requirements for the project.
    ```
    cd assessment
    pip install -r requirements.txt
    ```
4. Make your migrations, this will create a local DB for you based on "sqlite".
    ```
    python manage.py makemigrations
    pyhon manage.py migrate
    ```
5. You should now be able to run the application.
    ```
    python manage.py runserver
    ``` 

## How it works?

The API first checks the DB if the record already exists, if not, it calls another API `https://api.frankfurter.app/` underneath the hood where it checks for the given 3 query parameters and return a JSON response as follow:

- If `from`, `to` and `date` all exist, it returns a JSON response with a single key `rate` and value equals the exchange rate between the two currencies and stores this record in the DB.
    ```
    {
        rate: 1.755
    }    
    ```
- If `to` doesn't exist, it returns a JSON response with 2 keys:
    - `base` which is the from_currency, "EUR" by default if doesn't exist.
    - `rates` with a value of all possible to_currencies
    ```
    {
        base: "EUR",
        rates: {
            "USD": 1.025,
            "JPY": 85.12,
            "KRW": 3.1478
        }
    }
    ```
- If `date` doesn't exist, it returns JSON responses as above with the _**latest**_ exchange rates.
 
- If result is not found, it returns a _**404 NotFound**_ JSON response with a single message 
    ```
    {
        message: "Not found"
    }
    ```
    
## Test the application

After running the application, hit the endpoint `http://localhost:8000/rate/` with different query params where `from` & `to` takes a 3 letter string as "USD" or "EUR" and `date` takes a date formatted as _"yyyy-mm-dd"_. 

#### Optional: Admin page

> If you want to open the admin page to access the database and see changes:  
>       1. Create a superuser with `python manage.py createsuperuser`, you will be prompted to enter your credentials.  
>       2. Run the application `python manage.py runserver`.  
>       3. Hit `http://localhost:8000/admin/`, log in with your credentials.  
>       4. Click on the "Exchange" table and you will see the records.    
  
