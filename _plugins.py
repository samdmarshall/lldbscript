import os
import importlib
import _file


PLUGINS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Plugins');

MODULE_MAP = {};


def load_plugins(environment_dict):
    global MODULE_MAP;
    if _file.file_exists(PLUGINS_PATH) == False:
        _file.make_dir(PLUGINS_PATH);
    working_directory = os.getcwd();
    os.chdir(PLUGINS_PATH)
    for plugin in os.listdir(PLUGINS_PATH):
        if not plugin.startswith('.') and os.path.isfile(os.path.join(PLUGINS_PATH, plugin)):
            name = _file.get_file_name(plugin)
            if len(environment_dict) != 0 and not name in environment_dict:
                MODULE_MAP[name] = __import__(name);
            else:
                if not name in MODULE_MAP:
                    MODULE_MAP[name] = __import__(name);
                else:
                    reload(MODULE_MAP[name]);
            
    os.chdir(working_directory);


def get_plugin_list():
    global MODULE_MAP;
    return MODULE_MAP.keys();


def get_plugin_instance(name):
    global MODULE_MAP;
    return getattr(MODULE_MAP[name], name);


def get_plugin_path():
    return PLUGINS_PATH;