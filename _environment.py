import os


DEBUG_LOG_ENABLED_KEY = 'DEBUG_LOG_ENABLED';

ENVIRONMENT_VALUE_MAP = {
    DEBUG_LOG_ENABLED_KEY: str(False)
};


def debug_log_key():
    global DEBUG_LOG_ENABLED_KEY;
    return DEBUG_LOG_ENABLED_KEY;


def set_variable(name, value):
    global ENVIRONMENT_VALUE_MAP;
    ENVIRONMENT_VALUE_MAP[name] = value;


def has_variable(name):
    global ENVIRONMENT_VALUE_MAP;
    return name in ENVIRONMENT_VALUE_MAP;


def get_variable(name):
    global ENVIRONMENT_VALUE_MAP;
    return ENVIRONMENT_VALUE_MAP[name]


def debuglog():
    global ENVIRONMENT_VALUE_MAP;
    if has_variable(DEBUG_LOG_ENABLED_KEY):
        return get_variable(DEBUG_LOG_ENABLED_KEY);
    else:
        return False;