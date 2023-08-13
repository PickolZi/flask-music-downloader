# Spotify Music Downloader
Using Flask and other Python modules I will be creating a web application that can download music from Spotify.


&nbsp;
## How do I run this web application?
- First, you're going to have to run the redis database as well as celery worker, I made this easy for us by opening up the terminal and entering `docker compose up` to run both instances simultaneously.
- Next, you're going to need to install the modules(requirements) for the Flask application by running `pip install -r requirements.txt` to download all the required modules.
- Lastly, you have to run the ***run.py*** module, and then you're set to go.

Type `http://localhost:5000/user/pickolzhd` to start using my web application!


&nbsp;
## Resources
- [My Figma Design](https://www.figma.com/file/GNoDCRAU2lNReTHOHRA3H2/Spotify-music-downloader-web-app?type=design&node-id=0%3A1&mode=design&t=lyvvvRdU9YkTFWfl-1) - Learned Figma to design how my web application could/should look like.
- [Realtime Colors](https://realtimecolors.com/?colors=FFFFFF-000000-1ed760-121212-222222) - Found this website made by [juxtopposed](https://www.youtube.com/@juxtopposed) which helped simplify greatly what colors I should use.

&nbsp;
## Special thanks to the videos below for helping me with my web application
- [YT: Corey Schafer - Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&ab_channel=CoreySchafer) - Taught me the basics of Flask by creating a simple social media clone
- [YT: Pretty Printed - An Example of Celery in a Flask App With Multiple Files](https://www.youtube.com/watch?v=2j3em0QQaMg&ab_channel=PrettyPrinted) - Taught me how to download the songs asynchronously while running my Flask application by running a task queue application, Celery along with a redis database. 
- [YT: Jake Wright - Docker Compose in 12 Minutes](https://www.youtube.com/watch?v=Qw9zlE3t8Ko&t=230s&ab_channel=JakeWright) - Taught me how to run many different applications in a containerized environment by writing a single ***docker-compose*** file and building the images.

