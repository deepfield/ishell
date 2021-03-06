# -*- coding: utf-8 -*-

import sys
import ishell
import readline


def _print(msg=""):
    line_buffer = readline.get_line_buffer()
    # Clearing prompt
    sys.stdout.write("\r")
    if ishell._current_prompt:
        sys.stdout.write("\033[K")
    sys.stdout.write(str(msg))
    # Restoring prompt
    sys.stdout.write("\n")
    if ishell._current_prompt:
        sys.stdout.write(ishell._current_prompt)
    if line_buffer:
        sys.stdout.write(" %s" % line_buffer)
    sys.stdout.flush()
