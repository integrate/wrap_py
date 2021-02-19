# disable pygame Hello message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# set custom error handling
import sys
from wrap_py import _error_handling

sys.excepthook = _error_handling.python_error_hook

# load pygame constants to use directly
from pygame.locals import *

# translator for module strings
from wrap_py._transl import translator as _

# local application is created and initialized anyway
from wrap_py.wrap_world import wrap_world as world
from wrap_py.wrap_app import wrap_app as app
from wrap_py.wrap_event import wrap_event as event
from wrap_py.wrap_sprite import wrap_sprite as sprite
from wrap_py.wrap_sprite_text import wrap_sprite_text as text_sprite

# server types
SERVER_TYPE_LOCAL = 1000
SERVER_TYPE_THREAD = 1001

# reset local modules by remote
_initialized = False


def init(server_type=SERVER_TYPE_THREAD):
    global _initialized

    # no server required
    if server_type == SERVER_TYPE_LOCAL:
        _initialized = True
        return

    # reset submodules
    global world, app, event, sprite, text_sprite

    #server in other thread
    if server_type== SERVER_TYPE_THREAD:
        from wrap_py import _server_thread
        interfaces = [world, app, event, sprite, text_sprite]
        new_interfaces = _server_thread.start_app_thread(interfaces)
        world, app, event, sprite, text_sprite = new_interfaces

        _initialized = True
        return




from wrap_py import settings as st


def say_hi():
    print()
    print(_("Wrap_py uses these catalogs: "))
    print(st.DATA_PATH)
    print(st.DATA_PATH_ALT)
