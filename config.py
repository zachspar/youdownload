#!/usr/bin/env python3
"""Configuration file."""
import os


SECRET_KEY = b'\xeb4c\x1f\x8c\x7f\xd4\x1f\x0f\xf1\xb8\xd8\x8a<\xbf.vb?._\xcc\xe8\xf1'  # noqa: E501
STATIC_FOLDER = os.path.join(os.getcwd(),
                             'youdownload',
                             'static')
SONG_FOLDER = os.path.join(os.getcwd(),
                           'www', 'yd',
                           'songs', 'mp3')
