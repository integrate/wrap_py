from wrap_py import wrap_base


class wrap_app:
    @staticmethod
    def set_fps(fps):
        wrap_base.app.set_fps(fps)

    @staticmethod
    def start():
        wrap_base.app.start()