import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
from wrap_py import _error_handling
sys.excepthook = _error_handling.python_error_hook

from wrap_py import wrap_world as world, wrap_app as app, wrap_event as event
from wrap_py import wrap_sprite as sprite
from wrap_py import wrap_sprite_text as text_sprite
from wrap_py import settings as st
from wrap_py._transl import translator as _

#load pygame constants ro use directly
from pygame.locals import *


def say_hi():
    print()
    print(_("Wrap_py uses these catalogs: "))
    print(st.DATA_PATH)
    print(st.DATA_PATH_ALT)
