#!/usr/bin/env python3
from youdownload import app
from flask import (render_template, url_for, redirect)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", **{})

