#!/usr/bin/env python3
import os
from youdownload import app
from threading import Thread
from flask import (render_template, url_for, redirect,
                   request)
from youdownload.utilities.utils import download_song_from_url
from multiprocessing.pool import ThreadPool


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            youtube_url = request.form.get("youtube_url")

            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(download_song_from_url,
                                            (youtube_url,))
            ret_val = async_result.get()

            if not ret_val:
                return render_template("success.html", **{})

            return render_template("index.html", **ret_val)

        except Exception as e:
            print(e)

    return render_template("index.html", **{})

