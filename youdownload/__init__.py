#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

try:
    os.makedirs(os.path.join(os.getcwd(),
                             'www', 'yd',
                             'songs', 'mp3'))
    os.makedirs(os.path.join(os.getcwd(),
                             'youdownload',
                             'static'))
except OSError as e:
    print(e)


app.config.from_object('config')

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from youdownload.views.index import *
from youdownload.utilities.utils import *

