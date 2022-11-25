FROM python:3.9
COPY . /app
RUN pip3 install flask
WORKDIR /app
RUN echo "export ZONE=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)" >> run.sh
RUN echo "python3 -m flask run --host=0.0.0.0" >> run.sh
CMD ["sh", "run.sh"]
