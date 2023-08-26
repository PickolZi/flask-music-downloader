FROM python:3.11.4-bookworm
RUN apt-get update && apt-get install -y ffmpeg
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "run.py"]