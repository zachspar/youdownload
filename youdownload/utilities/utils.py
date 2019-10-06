#!/usr/bin/env python3
"""Youdownload utility functions."""
from __future__ import unicode_literals
import os
import youtube_dl
from youtube_dl.utils import DownloadError
from youdownload import app
from flask import render_template, send_from_directory, Response


OUTTMPL = os.path.join(os.getcwd(),
                       'www', 'yd',
                       'songs', 'mp3',
                       'downloaded_file.mp3')

DOWNLOAD_OPTIONS = {
    'outtmpl': OUTTMPL,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_song_from_url(url=None):
    """Download song from given video uri."""
    ctx = {
        "error": True,
        "msg": "",
    }
    try:
        if url:
            with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS) as ydl:
                title_result = ydl.extract_info(url)
                ydl.prepare_filename(title_result)
                # ydl.download([url])
                print("Audio downloaded successfully!")
                # TODO : fix bug here - file extension
                ctx["error"] = False
                ctx["song_filename"] = 'downloaded_song.mp3'
                return ctx
        print("NO URL PROVIDED")
        ctx["msg"] = "Not a valid URL!"
        return ctx
    except DownloadError as e:
        print(e)
        ctx["msg"] = e
        print("URL not specified...audio not downloaded")
        return ctx


@app.route('/static/<filename>', methods=["GET"])
def serve_file(filename):
    """Serve static files."""
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route('/download/<song_filename>', methods=["GET"])
def download_song(song_filename):
    """Download mp3 attachment."""
    return send_from_directory('/www/yd/songs/mp3/',
                               song_filename,
                               as_attachment=True,
                               mimetype="audio/mp3",
                               attachment_filename=song_filename)
