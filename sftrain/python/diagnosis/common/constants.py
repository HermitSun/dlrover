class InferenceConfigKey(object):
    LOG_FILE = "log_file"
    ERRORS = "errors"


class DiagnoseAction(object):
    NO_ACTION = "no_action"
    RESTART_WORKER = "restart_worker"
    RELAUNCH_WORKER = "relaunch_worker"
