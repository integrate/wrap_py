from wrap_py import server_service, server_class
from wrap_py import wrap_base

import threading


def start_server():
    # construct RPyC server
    hostname = '127.0.0.1'
    port = 18861
    server = server_class.RpycServer(app=wrap_base.app, service=server_service.MainService, hostname=hostname, port=port)

    #start in another thread
    thr = threading.Thread(target=server.start, daemon=True)
    thr.start()

    # start app in main thread
    wrap_base.app.start_as_server()


if __name__ == '__main__':
    start_server()
