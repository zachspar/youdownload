#!/usr/bin/env python3
"""Youdownload utility functions."""
from __future__ import unicode_literals
import os
import youtube_dl
from youtube_dl.utils import DownloadError
from youdownload import app
from werkzeug.utils import secure_filename
from flask import redirect, send_from_directory, url_for


FULL_PATH = os.path.join(os.getcwd(), 'www', 'yd', 'songs', 'mp3')
OUTTMPL = os.path.join(FULL_PATH, 'downloaded_song.mp3')  # TODO: change this!
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
                print("Audio downloaded successfully!")
                # TODO : fix bug here - file extension
                title = secure_filename(title_result.get("title", None))
                if '-' not in title:
                    artist = 'heap'
                else:
                    title = title.split('-')
                    artist = title[0].strip('_')
                    title = title[1].lstrip('_')
                    title = title.rstrip('_')
                save_to_file = '{}/{}/{}.mp3'\
                    .format(FULL_PATH, artist, title)
                os.system("mkdir -p {}/{}".format(FULL_PATH, artist))
                os.system("mv {}/downloaded_song.mp3 {}"
                          .format(FULL_PATH, save_to_file))
                ctx["error"] = False
                ctx["song_filename"] = '{}.mp3'.format(title)
                ctx["song_metadata"] = (artist, title)
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


@app.route('/download/<string:artist>/<string:title>', methods=["GET"])
def download_song(artist=None, title=None):
    """Download mp3 attachment."""
    if not title or not artist:
        return redirect(url_for('index'))
    print("Full path ::  [  {}  ]".format(FULL_PATH))
    path_to_song = '{}'.format(os.path.join(FULL_PATH, artist))
    song_filename = '{}.mp3'.format(title)
    return send_from_directory(path_to_song,
                               song_filename,
                               as_attachment=True,
                               mimetype="audio/mp3",
                               attachment_filename=song_filename)
