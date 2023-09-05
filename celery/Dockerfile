FROM python:3.11-bookworm
RUN apt-get update && apt-get install -y ffmpeg
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["celery", "-A", "run.celery", "worker", "-l", "INFO", "--pool=solo"]