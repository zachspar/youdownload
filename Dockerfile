from ubuntu:latest
maintainer Zachary Spar "zachspar@gmail.com"
workdir /
run apt-get update -y && \
    apt-get install -y python3-pip python3-dev
run mkdir /youdownload
copy config.py /
copy setup.py /
copy requirements.txt /
copy wsgi.py /
copy youdownload/ /youdownload
run pip3 install -r requirements.txt
cmd gunicorn --workers 2 --bind 0.0.0.0:8575 wsgi
