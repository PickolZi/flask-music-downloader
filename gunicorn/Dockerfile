FROM python:3.11.4-bookworm
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install gunicorn
RUN pip install -r requirements.txt
# The below command didn't work beause gunicorn was not recognized. Needed to run through a .sh file.
# CMD ["gunicorn","-w" "3","run:app","--bind" "0.0.0.0:8000"]
CMD ["bash", "./gunicorn/startup.sh"]