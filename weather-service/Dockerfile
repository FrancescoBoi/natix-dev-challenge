FROM python:3.11
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
#comment if not a package
ENV FLASK_APP=app 
ENV FLASK_RUN_HOST=0.0.0.0

#COPY app/weather.py ./
COPY app /app
EXPOSE 5000
#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD python weather.py #ok
CMD ["flask", "--app=routes", "run",  "--host=0.0.0.0", "--port=5000"]