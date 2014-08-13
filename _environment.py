import os

def setup_environment():
    set_variable('DEBUG_LOG_ENABLED', False);


def set_variable(name, value):
   os.putenv(name, value);


def has_variable(name):
    return os.environ.has_key(name);


def get_variable(name):
    return os.environ[name];


def debuglog():
    return get_variable('DEBUG_LOG_ENABLED');