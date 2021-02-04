import rpyc, subprocess, os, sys, time
from wrap_py import settings as st

#server process
proc = None

def _launch_server():
    global proc
    CREATE_NEW_CONSOLE =  0x00000010
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    flags = CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS

    d = os.path.split(__file__)[0]
    f = os.path.join(d, "server.py")

    ex_d = os.path.split(sys.executable)[0]
    ex_f = os.path.join(ex_d, "python")

    proc = subprocess.Popen([ex_f, f], creationflags=flags)


def init_remote():
    try:
        conn = rpyc.connect(st.SERVER_HOST_NAME, st.SERVER_PORT, keepalive=True)
    except:
        _launch_server()
        time.sleep(1)
        conn = rpyc.connect(st.SERVER_HOST_NAME, st.SERVER_PORT, keepalive=True)

    return conn

conn = init_remote()