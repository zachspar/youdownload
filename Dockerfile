from ubuntu:latest
maintainer Zachary Spar "zachspar@gmail.com"
run apt-get update -y && apt-get upgrade && \
    apt-get install -y python3-pip python3-dev
copy . /
workdir /
run pip3 install -r requirements.txt
entrypoint gunicorn 
cmd youdownload:app --workers 2
