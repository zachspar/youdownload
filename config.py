#!/usr/bin/env python3
"""Configuration file."""
import os


SECRET_KEY = b'your secret key here'
STATIC_FOLDER = os.path.join(os.getcwd(),
                             'youdownload',
                             'static')
SONG_FOLDER = os.path.join(os.getcwd(),
                           'www', 'yd',
                           'songs', 'mp3')
