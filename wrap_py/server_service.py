import rpyc
from wrap_py.wrap_world import wrap_world
from wrap_py.wrap_app import wrap_app
from wrap_py import event, sprite, text_sprite

def exposer(cls):
    for i in cls.__dict__.copy():
        if str(i).startswith("__") or str(i).startswith("_"):
            continue

        val = cls.__dict__[i]
        type(cls).__setattr__(cls, "exposed_"+str(i), val)

    return cls


class MainService(rpyc.Service):

    exposed_wrap_world = exposer(wrap_world)
    exposed_wrap_app = exposer(wrap_app)

    # def exposed_create_world(self, width, height):
    #     res = wrap_base.world.create_world(width, height)
    #     return res
    #
    # def exposed_add_sprite(self, sprite_type_name, x, y, visible=True, costume=None):
    #     res= wrap_sprite.add_sprite(sprite_type_name, x, y, visible, costume)
    #     return res


