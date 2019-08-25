#!/usr/bin/env python3
import os
from youdownload import app
from flask import (render_template, url_for, redirect,
                   request)
from youdownload.utilities.utils import download_song_from_url
from youtube_dl.utils import DownloadError


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")

        try:
            if download_song_from_url(youtube_url):
                return render_template("success.html",
                                       directory=app.config["TEMPLATE"])
        except DownloadError as e:
            print(e)
            ctx = {
                    "error": True,
                    "msg": str(e),
            }
            return render_template("index.html", **ctx)

    return render_template("index.html", **{})

