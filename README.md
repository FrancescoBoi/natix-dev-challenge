# HOW TO RUN
## Program execution
Run `sudo docker-compose up --build`.
In your host open the webrowser and to the url: https://localhost.com/weather?city=<your-city>

The project comprises a kafka producer that produces weather data, a kafka consumer which uses those data, a kafka broker, a web app in Flask which responds to http get requests, nd a Redis DB for readily access weather data.

Next step:
- use elastic search
- add SQL DB (SQLAlchemy)
- do some data transformations on the consumer and publish on redis to be used for the web-app
- add MongoDB
- Create alert Red and manage those from a Consumer
- add a second producer on a different city

## Pytest
Install pytest on your host or you virtualenvironment.
To run pytests go to `dev-challenge/weather-service` and run `pytest` or `pytest tests/`. 


# PROJECT STRUCTURE
```
./
├── app
│   ├── __init__.py: initialises Redis and Flask
│   ├── externals.py: simulates external calls
│   ├── routes.py: app endpoints
│   └── structures.py: file containing custom classes for type hinting
├── tests
│   ├── conftest.py: config file for mocking Redis, etc.
│   └── test_app.py: unit test file
├── docker-compose.yaml
├── Dockerfile
├── pytest.ini
├── readme.md
└── requirements.txt
```
