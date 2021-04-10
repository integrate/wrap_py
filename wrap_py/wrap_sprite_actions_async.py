import time
import wrap_py

sprite = wrap_py.sprite
event = wrap_py.event


def _reset_global_interfaces():
    global sprite, event
    sprite = wrap_py.sprite
    event = wrap_py.event


def _calc_values_by_percent(changing_kwargs: dict, percent):
    """
    updates changing_kwargs "val" key accordingly to percent

    :param changing_kwargs:
    :param percent:
    :return:
    """
    for arg_dict in changing_kwargs.values():
        arg_dict['val'] = arg_dict['start'] + (arg_dict['stop'] - arg_dict['start']) * percent


def _get_changing_kwargs(changing_kwargs, use_stop_values):
    """
    return flat dict {'param_name':param_value}

    :param changing_kwargs:
    :param use_stop_values:
    :return:
    """
    key = "stop" if use_stop_values else "val"
    ch_kw = {name: int(d[key]) for (name, d) in changing_kwargs.items()}
    return ch_kw


class wrap_sprite_actions_async():
    mult_fps = 100

    @staticmethod
    def _start_action(func, fixed_kwargs: dict, changing_kwargs: dict, time_ms: int, fps: int, on_before_action=None,
                      on_after_action=None):
        """changing_kwargs:{
            "argname1":{
                start: int,
                stop: int
            }
        }
        """

        def _action_callback():
            nonlocal finished

            if finished: return

            # percent of time length passed
            passed_percent = (time.time() - start_time) / time_length

            # if all time passed - nothing to do here
            if passed_percent >= 1:
                finished = True

                ch_kw = _get_changing_kwargs(changing_kwargs, True)
                func(**fixed_kwargs, **ch_kw)

                event.stop_listening(event_id)
                return

            # update values
            _calc_values_by_percent(changing_kwargs, passed_percent)
            ch_kw = _get_changing_kwargs(changing_kwargs, False)

            # check if can continue
            if on_before_action is not None and not on_before_action(**fixed_kwargs, **ch_kw):
                finished = True
                event.stop_listening(event_id)
                return

            # make action
            func(**fixed_kwargs, **ch_kw)

            # check if can continue
            if on_after_action is not None and not on_after_action(**fixed_kwargs, **ch_kw):
                finished = True
                event.stop_listening(event_id)
                return

        start_time = time.time()
        time_length = time_ms / 1000
        end_time = start_time + time_length

        step_delay = 1 / fps

        finished = False

        event_id = event.register_event_handler(_action_callback, int(step_delay*1000))


    @staticmethod
    def change_sprite_size(id, time_ms, width, height, on_before_action=None, on_after_action=None):
        start_width, start_height = sprite.get_sprite_size(id)

        f = sprite.change_sprite_size
        fixkw = {"id": id}
        chkw = {
            "width": {"start": start_width, "stop": width},
            "height": {"start": start_height, "stop": height}
        }
        cls._start_action(f, fixkw, chkw, time_ms, cls.mult_fps, on_before_action, on_after_action)

    @staticmethod
    def change_sprite_width(id, time_ms, width, on_before_action=None, on_after_action=None):
        start_width = sprite.get_sprite_width(id)

        f = sprite.change_sprite_width
        fixkw = {"id": id}
        chkw = {
            "width": {"start": start_width, "stop": width}
        }
        cls._start_action(f, fixkw, chkw, time_ms, cls.mult_fps, on_before_action, on_after_action)

    @staticmethod
    def change_sprite_height(id, time_ms, height, on_before_action=None, on_after_action=None):
        start_height = sprite.get_sprite_height(id)

        f = sprite.change_sprite_height
        fixkw = {"id": id}
        chkw = {
            "height": {"start": start_height, "stop": height}
        }
        cls._start_action(f, fixkw, chkw, time_ms, cls.mult_fps, on_before_action, on_after_action)


cls = wrap_sprite_actions_async