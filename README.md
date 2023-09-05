# Spotify Music Downloader
Using Flask and other Python modules I will be creating a web application that can download music from Spotify.


&nbsp;
## How do I run this web application?
- First, you will have to edit the "SAMPLE_SECRETS.json" file, renaming it to "SECRETS.json". There should be 3 keys named, "SPOTIFY_FLASK_SECRET_KEY", "SPOTIFY_KEY", "SPOTIFY_SECRET. Which will be your Flask secret key, then the Spotify API Developer key and secret in order. Note you will need an active [Spotify Developer account](https://developer.spotify.com/dashboard) for this. 
- Next, you're going to have to run the redis database, celery worker, as well as the gunicorn/NGINX web server application, I made this easy for us by opening up the terminal and entering `docker compose up` to download and run all microservices simultaneously. Note you will need [docker](https://docs.docker.com/get-docker/) installed on your device.
- Lastly, after all the docker containers are up and running, type `http://localhost` to start using my Spotify Music Downloader web application!


&nbsp;
## Resources
- [My Figma Design](https://www.figma.com/file/GNoDCRAU2lNReTHOHRA3H2/Spotify-music-downloader-web-app?type=design&node-id=0%3A1&mode=design&t=lyvvvRdU9YkTFWfl-1) - Learned Figma to design how my web application could/should look like.
- [Realtime Colors](https://realtimecolors.com/?colors=FFFFFF-000000-1ed760-121212-222222) - Found this website made by [juxtopposed](https://www.youtube.com/@juxtopposed) which helped simplify greatly what colors I should use.

&nbsp;
## Special thanks to the videos below for helping me with my web application
- [YT: Corey Schafer - Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&ab_channel=CoreySchafer) - Taught me the basics of Flask by creating a simple social media clone
- [YT: Pretty Printed - An Example of Celery in a Flask App With Multiple Files](https://www.youtube.com/watch?v=2j3em0QQaMg&ab_channel=PrettyPrinted) - Taught me how to download the songs asynchronously while running my Flask application by running a task queue application, Celery along with a redis database. 
- [YT: Jake Wright - Docker Compose in 12 Minutes](https://www.youtube.com/watch?v=Qw9zlE3t8Ko&t=230s&ab_channel=JakeWright) - Taught me how to run many different applications in a containerized environment by writing a single ***docker-compose*** file and building the images.

