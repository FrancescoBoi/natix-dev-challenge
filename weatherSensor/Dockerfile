FROM python:3.11

RUN pip install --upgrade pip
WORKDIR /weatherSensor

#COPY requirements.txt .
COPY weatherSensor /weatherSensor
RUN pip install -r /weatherSensor/requirements.txt

# Set environment variables
#comment if not a package
#COPY app/weatherSe.py ./
#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD python weather.py #ok
CMD ["python", "-u", "weather_sensor.py"]