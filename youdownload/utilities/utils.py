#!/usr/bin/env python3
from __future__ import unicode_literals
import os
import youtube_dl
from youtube_dl.utils import DownloadError
from youdownload import app
from flask import render_template


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
    try:
        if url:
            with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS) as ydl:
                ydl.download([url])
                print("Audio downloaded successfully!")
                return None
            print("NO URL PROVIDED")
    except DownloadError as e:
        print(e)
        ctx = {
                "error": True,
                "msg": str(e),
        }

        print("URL not specified...audio not downloaded")
        return ctx

