import rpyc, time

class RpycServer(rpyc.ThreadedServer):
    def __init__(self, app, *args, **kwargs):
        rpyc.ThreadedServer.__init__(self, *args, **kwargs)
        self._app = app

    def _handle_connection(self, conn):
        self._app.add_connection(conn)
        while not conn.closed:
            time.sleep(1/100)
        self._app.remove_connection(conn)
