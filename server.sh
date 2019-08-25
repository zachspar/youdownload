#!/bin/bash
export FLASK_APP=youdownload
export FLASK_ENV=development

CWD=$(pwd)
if [ ! -d $CWD/www/yd/songs/mp3 ] ;
then
    echo "Directory [$CWD/www/yd/songs/mp3] does not exist..."
    echo "Making directories for saved songs from youtube..."
    mkdir -p $CWD/www/yd/songs/mp3
    echo "DONE."
fi

echo "Adding environment variable YD_OUTTMPL"
export YD_OUTTMPL="$CWD/www/yd/songs/mp3/%(title)s.%(ext)s"

flask run

