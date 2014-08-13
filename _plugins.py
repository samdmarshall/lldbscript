import os
import importlib
import pkgutil

import _lldbcmd
import _file


PLUGINS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Plugins');

MODULE_MAP = {};


def load(environment_dict):
    global MODULE_MAP;
    if _file.file_exists(PLUGINS_PATH) == False:
        _file.make_dir(PLUGINS_PATH);
    working_directory = os.getcwd();
    os.chdir(PLUGINS_PATH)
    for plugin in os.listdir(PLUGINS_PATH):
        if not plugin.startswith('.') and os.path.isfile(os.path.join(PLUGINS_PATH, plugin)):
            name = _file.get_file_name(plugin)
            if not name in environment_dict:
                MODULE_MAP[name] = getattr(__import__(name), name);
            
    os.chdir(working_directory);


def get_plugin_list():
    global MODULE_MAP;
    return MODULE_MAP.keys();


def get_plugin_instance(name):
    global MODULE_MAP;
    return MODULE_MAP[name];