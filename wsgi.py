#!/usr/bin/env python3
"""Serve flask app using gunicorn."""
from youdownload import app as application


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8575)
