#!/usr/bin/env python3
"""Create flask app."""
import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

try:
    full_path = os.path.join(os.getcwd(), 'www', 'yd', 'songs', 'mp3')
    os.makedirs(full_path)
    os.makedirs(os.path.join(os.getcwd(), 'youdownload', 'static'))
except OSError as e:
    print(e)
finally:
    os.system('rm -f {}/downloaded_song*'.format(full_path))

app.config.from_object('config')

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from youdownload.views.index import *  # noqa: E402
from youdownload.utilities.utils import *  # noqa: E402
