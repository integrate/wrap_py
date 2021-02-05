from wrap_py import server_service, server_class
from wrap_py import wrap_base, settings as st

import sys, threading


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


def start_server_pipes():
    import rpyc
    conn = rpyc.connect_stdpipes(service = server_service.MainService)
    wrap_base.app.start_with_connection(conn)

if __name__ == '__main__':
    args = sys.argv[1:]
    if "--pipes" in args:
        start_server_pipes()
    else:
        start_server()
