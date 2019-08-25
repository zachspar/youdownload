#!/usr/bin/env python3
from __future__ import unicode_literals
import os
import youtube_dl
from youdownload import app


DOWNLOAD_OPTIONS = {
    'outtmpl' : app.config["TEMPLATE"],
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_song_from_url(url=None):
    print("Thread started")
    print("Thread :: Downling audio from [{}]".format(url))
    if url:
        with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS) as ydl:
            ydl.download([url])
            print("Audio downloaded successfully!")
            return

    print("URL not specified...audio not downloaded")

