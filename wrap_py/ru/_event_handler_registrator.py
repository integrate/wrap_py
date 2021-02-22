from wrap_py import _event_handler_registrator as ehr

def vsegda(zaderzhka=100):
    return ehr.always(zaderzhka)