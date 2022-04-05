FROM python:3.7-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#RUN apt-get update && apt-get install -y python3-opencv
#RUN pip install opencv-python
EXPOSE 5001
ENTRYPOINT FLASK_APP=/app/app.py flask run --host 0.0.0.0