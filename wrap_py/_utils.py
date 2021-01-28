from wrap_py._transl import translator as _
from wrap_engine.exception import WrapEngineExceprion

def _print_error(errtext):
    err = _("Error!")

    print("")
    print("\033[91m" + err + " " + str(errtext))
    exit()

def error_decorator(orig_func):
    def new_func(*args,**kwargs):
        try:
            return orig_func(*args,**kwargs)

        except Exception as e:
            _print_error(_(str(e)))

    return new_func