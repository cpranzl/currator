#!/usr/bin/env python3

import os, sys
from PIL import Image

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


for infile in sys.argv[1:]:
    print(get_date_taken(infile))

