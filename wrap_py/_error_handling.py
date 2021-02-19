from wrap_py._transl import translator as _
from wrap_py import settings
from wrap_engine.exception import WrapEngineExceprion
import sys, inspect, os
import colorama
from colorama import Fore, Back, Style

def get_tb_data(traceback):
    tb_data = {}

    frame_info = inspect.getframeinfo(traceback.tb_frame)
    tb_data['filename'] = frame_info.filename
    tb_data['lineno'] = frame_info.lineno
    tb_data['function'] = frame_info.function

    module_name = os.path.split(frame_info.filename)[1]
    module_name = os.path.splitext(module_name)[0]
    tb_data['module_name'] = module_name

    code_lines = []
    if frame_info.code_context is not None:
        for i in frame_info.code_context:
            code_lines.append(str(i).strip())
    tb_data['code_lines'] = code_lines

    return tb_data


def get_traceback_list(traceback):
    # convert to list
    tb_list = []
    while traceback is not None:
        tb_list.append(get_tb_data(traceback))
        traceback = traceback.tb_next

    return tb_list


def filter_traceback_list(tb_list):
    # filter out last error handler entry
    this_module_name = __name__.split(".")[-1]
    tb_data = tb_list[-1]
    if tb_data['module_name'] == this_module_name:
        del tb_list[-1]

    #filterout wrap_engine frames
    for tb_data in tb_list.copy():
        if tb_data['function'].startswith(settings.ENGINE_NAME):
            tb_list.remove(tb_data)

    return tb_list


def make_console_link_to_code(filename, lineno):
    return "File \"" + str(filename) + "\", line " + str(lineno)


def python_error_hook(type, value, traceback):
    colorama.init()

    w_module = _("module")
    w_line = _("line of code")
    w_func = _("function")
    w_code = _("code")
    w_error = _("error")
    w_callstack = _("call stack")
    code_tab = "  "

    print()
    print(Fore.RED + w_callstack.capitalize() + ":")
    print(Fore.RED + Back.RESET + "".rjust(100, "-"))

    tb_list = get_traceback_list(traceback)
    tb_list = filter_traceback_list(tb_list)
    for tb_data in tb_list:
        link_text = make_console_link_to_code(tb_data["filename"], tb_data["lineno"])
        # print error
        print(Fore.RED, Back.RESET)

        print(link_text)
        print(w_module.capitalize().ljust(15, " ") + ":", tb_data["module_name"])
        print(w_func.capitalize().ljust(15, " ") + ":", tb_data["function"])

        code_lines = tb_data['code_lines']
        if len(code_lines) > 0:
            print(w_code.capitalize().ljust(15, " ") + ":")
            for i in code_lines:
                print(code_tab, Style.BRIGHT, Fore.GREEN, Back.RESET, i, Fore.RESET, Back.RESET, Style.RESET_ALL)

        print(Fore.RED + Back.RESET + "".rjust(100, "-"))

    print(Fore.RED)
    print(w_error.capitalize() + ":", Fore.GREEN, Style.BRIGHT, _(str(value)).strip())
    print(Fore.RED + Back.RESET + "".rjust(100, "-"))
