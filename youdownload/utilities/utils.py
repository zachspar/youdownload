#!/usr/bin/env python3
from __future__ import unicode_literals
import os
import youtube_dl
from youtube_dl.utils import DownloadError
from youdownload import app
from flask import render_template, send_from_directory, Response



OUTTMPL = os.path.join(os.getcwd(),
                       'www', 'yd',
                       'songs', 'mp3',
                       '%(title)s.%(ext)s')

DOWNLOAD_OPTIONS = {
    'outtmpl' : OUTTMPL,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_song_from_url(url=None):
    ctx = {
        "error": True,
        "msg": "",
    }
    try:
        if url:
            with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS) as ydl:
                title_result = ydl.extract_info(url)
                ydl.prepare_filename(title_result)
                title = title_result.get("title", None) + ".mp3"
                # ydl.download([url])
                print("Audio downloaded successfully!")
                # TODO : fix bug here - file extension
                ctx["error"] = False
                ctx["song_filename"] = title
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
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route('/download/<song_filename>', methods=["GET"])
def download_song(song_filename):
    return send_from_directory(app.config["SONG_FOLDER"],
                               song_filename,
                               as_attachment=True,
                               mimetype="audio/mp3",
                               attachment_filename=song_filename)

