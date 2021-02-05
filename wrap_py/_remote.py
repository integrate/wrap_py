import rpyc, subprocess, os, sys, time
from wrap_py import settings as st

SERVER_TYPE_NETWORK = 1
SERVER_TYPE_PIPES = 2

def _launch_server(script_params=[], popen_kwargs={}, pythonw = False, separate_process=False):

    if separate_process:
        CREATE_NEW_CONSOLE =  0x00000010
        DETACHED_PROCESS = 0x00000008
        CREATE_NEW_PROCESS_GROUP = 0x00000200

        flags = CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS
    else:
        flags = 0

    python_name = "pythonw" if pythonw else "python"

    d = os.path.split(__file__)[0]
    f = os.path.join(d, "server.py")

    ex_d = os.path.split(sys.executable)[0]
    ex_f = os.path.join(ex_d, python_name)

    return subprocess.Popen([ex_f, f, *script_params], creationflags=flags, **popen_kwargs)


def _init_remote_network():
    try:
        conn = rpyc.connect(st.SERVER_HOST_NAME, st.SERVER_PORT, keepalive=True)
    except:
        try:
            _launch_server(separate_process=True, pythonw=False)
            time.sleep(1)
            conn = rpyc.connect(st.SERVER_HOST_NAME, st.SERVER_PORT, keepalive=True)
        except:
            return False

    return conn

def _init_remote_pipes():
    try:
        proc = _launch_server(script_params=["--pipes"],
                              popen_kwargs={"stdin":subprocess.PIPE, "stdout":subprocess.PIPE},
                              pythonw=True,
                              separate_process=False)
        conn = rpyc.connect_pipes(proc.stdout, proc.stdin)
    except:
        return False

    conn.proc = proc
    return conn

def init_remote(server_type=SERVER_TYPE_PIPES):
    if server_type == SERVER_TYPE_NETWORK:
        return _init_remote_network()
    elif server_type == SERVER_TYPE_PIPES:
        return _init_remote_pipes()