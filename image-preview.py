#!/usr/bin/env python
"""
w3mimgdisplay wrapper

Usage: image-preview.py w3mimgdisplay_path [ files ... ]

Only jpeg, jpg, png and gif files are processed.
"""

from sys import argv
import re
import subprocess
import itertools
import os.path
from os import getenv

def get_terminal_size():
    import sys, struct, fcntl, termios
    _, _, w, h = struct.unpack("HHHH",
                               fcntl.ioctl(sys.stderr.fileno(), # stderr is not redirected, unlike stdout
                                           termios.TIOCGWINSZ,
                                           struct.pack("HHHH",
                                                       0,0,0,0)))
    return w, h


def main():
    ##########  CONFIG BEGIN  ##########
    upper_margin  = 50
    max_height    = 300
    width         = 270
    images_in_row = 5
    max_rows      = 3
    border        = 5
    autodetect_size = bool(getenv("DISPLAY")) # we are in X and not tty
    ##########   CONFIG END   ##########


    w3mimgdisplay = argv.pop(1)
    argv.pop(0)

    # calculate how many images can we fit horizontally
    if autodetect_size:
        term_w, term_h = get_terminal_size()
        term_h -= upper_margin
        images_in_row = term_w // (width + border)

    # lazily get at max as many elements, as we can display, while removing non-images
    args = list(itertools.islice((arg
                                  for arg in argv
                                  if arg.strip()
                                  and os.path.isfile(arg)
                                  and re.search(r"\.jpe?g$|\.png$|\.bmp$|\.gif$",
                                                arg, re.IGNORECASE)),
                                 0, images_in_row * max_rows))

    if not args:
        exit(1)

    # calculate the maximum image width that will still let us fit images_in_row images
    if autodetect_size:
        width = term_w // min(images_in_row, len(args)) - border
        if len(args) <= images_in_row:
            max_height = term_h
        else:
            # do not scale later to fit the image vertically
            autodetect_size = False

    column = 0
    row = 0
    for arg in args:
        w3m = subprocess.Popen([w3mimgdisplay],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)
        result = w3m.communicate("5;{0}".format(arg).encode())[0].decode()
        if result.strip():
            w, h = [int(string)
                    for string
                    in result.split()]
            w_scaled = min(width, w)
            h_scaled = (w_scaled * h) // w
            if autodetect_size and h_scaled > term_h:
                h_scaled = term_h
                w_scaled = (h_scaled * w) // h
            print("2;3;\n0;1;{x};{y};{w};{h};0;0;0;{h_max};{path}\n4;\n3;".format(
                x = column * (width + border),
                y = upper_margin + row * (max_height + border),
                w = w_scaled,
                h = h_scaled,
                h_max = max_height,
                path = arg))
            column = (column+1) % images_in_row
            if column == 0:
                row += 1

if __name__ == "__main__":
    main()
