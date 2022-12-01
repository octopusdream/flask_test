FROM python:3.9
COPY . /app
RUN pip3 install flask 
RUN pip3 install prometheus-flask-exporter
WORKDIR /app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
