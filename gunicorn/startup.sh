#!/bin/sh
# Runs gunicorn web server, because dockerfile does not let me run it through command line.
cd /usr/src/app
gunicorn -w 3 --bind 0.0.0.0:8000 run:app