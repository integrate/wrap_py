import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
from wrap_py import _error_handling
sys.excepthook = _error_handling.python_error_hook

from wrap_py import settings as st
from wrap_py._transl import translator as _

#load pygame constants ro use directly
from pygame.locals import *


def say_hi():
    print()
    print(_("Wrap_py uses these catalogs: "))
    print(st.DATA_PATH)
    print(st.DATA_PATH_ALT)


#local modules to use from outside
from wrap_py.wrap_world import wrap_world as world
from wrap_py.wrap_app import wrap_app as app
from wrap_py import wrap_event as event
from wrap_py import wrap_sprite as sprite
from wrap_py import wrap_sprite_text as text_sprite

#server types
from wrap_py._remote import SERVER_TYPE_PIPES, SERVER_TYPE_NETWORK

#reset local modules from remote
def init_remote(server_type = SERVER_TYPE_PIPES):
    global world
    from wrap_py import _remote
    conn = _remote.init_remote(server_type)
    if not conn:
        print(_("Server starting error"))
        return

    world = conn.root.wrap_world
    app = conn.root.wrap_app
