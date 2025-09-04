FROM python:3.11

RUN pip install --upgrade pip
WORKDIR /app

#COPY app/weather.py ./
COPY app /app
COPY ./structures/redis_structures.py /app
RUN pip install -r /app/requirements.txt

# Set environment variables
#comment if not a package
ENV FLASK_APP=app 
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD python weather.py #ok
CMD ["flask", "--app=routes", "run",  "--host=0.0.0.0", "--port=5000"]