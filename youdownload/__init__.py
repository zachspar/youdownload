#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(SECRET_KEY='dev',
                        TEMPLATE=os.environ.get('YD_OUTTMPL'),
                        CWD=os.getcwd())

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from youdownload.views.index import *
from youdownload.utilities.utils import *

