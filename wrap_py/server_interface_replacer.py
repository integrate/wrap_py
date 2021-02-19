class ServerInterfaceReplacer():
    def __init__(self, remote_obj):
        self._orig = remote_obj

    def __getattr__(self, item):
        if item in type(self).__dict__:
            return type(self).__dict__[item]

        if item in dir(self._orig):
            return getattr(self._orig, item)

        return super().__getattribute__(item)