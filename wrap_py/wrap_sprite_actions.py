import time
import wrap_py

sprite = wrap_py.sprite
def _reset_global_interfaces():
    global sprite
    sprite = wrap_py.sprite

class wrap_sprite_actions():
    mult_fps = 100

    @staticmethod
    def _make_calls_with_delay(func, fixed_kwargs: dict, changing_kwargs: dict, time_ms: int, fps: int):
        """changing_kwargs:{
            "argname1":{
                start: int,
                stop: int
            }
        }
        """

        start_time = time.time()
        time_length = time_ms / 1000
        end_time = start_time + time_length

        step_delay = 1/fps

        now = time.time()
        while now<end_time:

            #percent of time length passed
            passed_percent = (time.time() - start_time)/time_length

            #if all time passed - nothing to do here
            if passed_percent>=1:
                break

            # change all values proportionally to passed time
            for arg_dict in changing_kwargs.values():
                arg_dict['val'] = arg_dict['start'] + (arg_dict['stop'] - arg_dict['start'])*passed_percent

            ch_kw = {name: int(d['val']) for (name, d) in changing_kwargs.items()}
            func(**fixed_kwargs, **ch_kw)

            #wait for next step
            if now+step_delay>time.time():
                time.sleep(now+step_delay-time.time())

            now = time.time()

        # final call with final values
        ch_kw = {name: int(d['stop']) for (name, d) in changing_kwargs.items()}
        func(**fixed_kwargs, **ch_kw)


    @classmethod
    def change_sprite_size(cls, id, time_ms, width, height):
        start_width, start_height = sprite.get_sprite_size(id)

        f = sprite.change_sprite_size
        fixkw = {"id":id}
        chkw = {
            "width": {"start": start_width, "stop": width},
            "height": {"start": start_height, "stop": height}
        }
        cls._make_calls_with_delay(f, fixkw, chkw, time_ms, cls.mult_fps)

    @classmethod
    def change_sprite_width(cls, id, time_ms, width):
        start_width = sprite.get_sprite_width(id)

        f = sprite.change_sprite_width
        fixkw = {"id":id}
        chkw = {
            "width": {"start": start_width, "stop": width}
        }
        cls._make_calls_with_delay(f, fixkw, chkw, time_ms, cls.mult_fps)

    @classmethod
    def change_sprite_height(cls, id, time_ms, height):
        start_height = sprite.get_sprite_height(id)

        f = sprite.change_sprite_height
        fixkw = {"id":id}
        chkw = {
            "height": {"start": start_height, "stop": height}
        }
        cls._make_calls_with_delay(f, fixkw, chkw, time_ms, cls.mult_fps)
