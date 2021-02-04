from wrap_py import server_service, server_class
from wrap_py import wrap_base, settings as st

import threading


def start_server():
    # construct RPyC server
    server = server_class.RpycServer(app=wrap_base.app, service=server_service.MainService, hostname=st.SERVER_HOST_NAME, port=st.SERVER_PORT)

    #start in another thread
    thr = threading.Thread(target=server.start)
    thr.start()

    # start app in main thread
    try:
        wrap_base.app.start_as_server()
    finally:
        server.close()


if __name__ == '__main__':
    start_server()
