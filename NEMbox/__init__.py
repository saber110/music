#!/usr/bin/env python
# encoding: UTF-8
'''
网易云音乐 Entry
'''
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()

import curses
import traceback
import argparse
import sys

from .menu import Menu
version = "0.2.4.2"


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        help="show this version and exit",
                        action="store_true")
    parser.add_argument("--search",
                        help="search song",
                        action="store")
    args = parser.parse_args()
    if args.version:
        latest = Menu().check_version()
        curses.endwin()
        print('NetEase-MusicBox installed version:' + version)
        if latest != version:
            print('NetEase-MusicBox latest version:' + str(latest))
        sys.exit()

    if args.search is not None:
        nembox_menu = Menu()
        nembox_menu.search(args.search)
        sys.exit()

    nembox_menu = Menu()
    try:
        nembox_menu.start_fork(version)
    except (OSError, TypeError, ValueError, KeyError):
        # clean up terminal while failed
        nembox_menu.screen.keypad(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()


if __name__ == '__main__':
    start()
