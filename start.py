#!/usr/bin/env python
# vim:fileencoding=utf-8
## If `./start.py` doesn't work for you, try `python3 start.py`.

import sys

from matebot import bot

if __name__ == "__main__":
  mode = 'cli'
  config_file = 'matebot'
  if len(sys.argv) > 1:
    mode = sys.argv[1]
    if len(sys.argv) > 2:
      config_file = sys.argv[2]
  bot(mode, config_file)

