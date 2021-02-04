import rpyc, psutil, subprocess, os, sys

def _launch_server():
    CREATE_NEW_CONSOLE =  0x00000010
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    flags = CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS

    d = os.path.split(__file__)[0]
    f = os.path.join(d, "server.py")

    ex_d = os.path.split(sys.executable)[0]
    ex_f = os.path.join(ex_d, "pythonw")
    proc = subprocess.Popen([ex_f, f], creationflags=flags)


def init_remote():
    import time

    try:
        conn = rpyc.connect('127.0.0.1', 18861)
    except:
        _launch_server()
        conn = rpyc.connect('127.0.0.1', 18861)

    return conn

conn = init_remote()