FROM python:3.11

RUN pip install --upgrade pip
WORKDIR /transformer

#COPY requirements.txt .
COPY transformer /transformer
RUN pip install -r /transformer/requirements.txt

# Set environment variables
#comment if not a package
#COPY app/weatherSe.py ./
#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD python weather.py #ok
CMD ["python", "-u", "transformer.py"]