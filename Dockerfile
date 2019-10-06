from ubuntu:latest
maintainer Zachary Spar "zachspar@gmail.com"
workdir /
run apt-get update -y && \
    apt-get install -y python3-pip python3-dev ffmpeg
run mkdir -p /youdownload /www/yd/songs/mp3
copy config.py /
copy setup.py /
copy requirements.txt /
copy wsgi.py /
copy youdownload/ /youdownload
run pip3 install -r requirements.txt
env YD_OUTTMPL /www/yd/songs/mp3/downloaded_song.mp3
cmd gunicorn --workers 2 --bind 0.0.0.0:5000 wsgi
