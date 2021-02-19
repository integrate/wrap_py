# disable pygame Hello message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# set custom error handling
import sys, threading
from wrap_py import _error_handling

sys.excepthook = _error_handling.python_error_hook
threading.excepthook = _error_handling.threading_error_hook

# load pygame constants to use directly
from pygame.locals import *

# translator for module strings
from wrap_py._transl import translator as _

# local application is created and initialized anyway
from wrap_py import wrap_world
from wrap_py import wrap_app
from wrap_py import wrap_event
from wrap_py import wrap_sprite
from wrap_py import wrap_sprite_text
world = wrap_world.wrap_world
app = wrap_app.wrap_app
event = wrap_event.wrap_event
sprite = wrap_sprite.wrap_sprite
text_sprite = wrap_sprite_text.wrap_sprite_text


# server types
SERVER_TYPE_LOCAL = 1000
SERVER_TYPE_THREAD = 1001

# reset local modules by remote
_initialized = False


def init(server_type=SERVER_TYPE_THREAD):
    global _initialized
    # reset submodules
    global world, app, event, sprite, text_sprite

    #only initialize once. No way to stop launched threads.
    if _initialized:
        return

    # no server required
    if server_type == SERVER_TYPE_LOCAL:
        world = wrap_world.wrap_world
        app = wrap_app.wrap_app
        event = wrap_event.wrap_event
        sprite = wrap_sprite.wrap_sprite
        text_sprite = wrap_sprite_text.wrap_sprite_text
        _initialized = True
        return

    #server in other thread
    if server_type== SERVER_TYPE_THREAD:
        from wrap_py import _server_thread

        interfaces = [world, app, event, sprite, text_sprite]
        res = _server_thread.start_app_thread(interfaces)

        world, app, event, sprite, text_sprite = res['patched_interfaces']
        wrap_event.event_handler_hook = res['callback_func_patcher']

        _initialized = True
        return




from wrap_py import settings as st


def say_hi():
    print()
    print(_("Wrap_py uses these catalogs: "))
    print(st.DATA_PATH)
    print(st.DATA_PATH_ALT)
