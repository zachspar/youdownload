#!/usr/bin/env python3
import os
from threading import Thread
from youdownload import app
from flask import (render_template, url_for, redirect,
                   request)
from youdownload.utilities.utils import download_song_from_url


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")

        download_thread = Thread(target=download_song_from_url,
                                 args=(youtube_url,))
        download_thread.start()
        download_thread.join()
        return render_template("success.html",
                               directory=app.config["TEMPLATE"])

    return render_template("index.html", **{})

