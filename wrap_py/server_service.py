import rpyc
from wrap_py.wrap_world import wrap_world
from wrap_py.wrap_app import wrap_app
from wrap_py.wrap_event import wrap_event
from wrap_py.wrap_sprite import wrap_sprite
from wrap_py.wrap_sprite_text import wrap_sprite_text

def exposer(cls):
    for i in cls.__dict__.copy():
        if str(i).startswith("__") or str(i).startswith("_"):
            continue

        val = cls.__dict__[i]
        if hasattr(val, "hide_on_server") and val.hide_on_server:
            continue

        type(cls).__setattr__(cls, "exposed_"+str(i), val)

    return cls


class MainService(rpyc.Service):
    exposed_wrap_world = exposer(wrap_world)
    exposed_wrap_app = exposer(wrap_app)
    exposed_wrap_event = exposer(wrap_event)
    exposed_wrap_sprite = exposer(wrap_sprite)
    exposed_text_sprite = exposer(wrap_sprite_text)