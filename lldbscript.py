#!/usr/bin/env python

import os

import _string
import _colours
import _print
import _lldbcmd
import _templatescript
import _plugins
import _file
import _environment
import _cmdmap


CORE_SCRIPT_NAMES = ['_colours.py', '_string.py', '_print.py', '_lldbcmd.py', '_environment.py', '_templatescript.py', '_file.py', '_plugins.py', '_cmdmap.py'];

INTERNAL_LOADED_NAME_CHECK = '__INTERNAL_LLDBSCRIPT_LOAD_CHECK'


def build_script_path(script_name):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), script_name);


def reload_scripts(environment_dict):
    for script in CORE_SCRIPT_NAMES:
        if not _file.get_file_name(script) in environment_dict:
            script_path = build_script_path(script);
            _lldbcmd.execute_command('script', '', 'import', script_path);


def __lldb_init_module(debugger, environment_dict):
    if not INTERNAL_LOADED_NAME_CHECK in environment_dict:
        _print.fmt([_print.Colour('blue', True), _print.Colour('bold', True), _print.String('%s', 'Loading lldbscript...'), _print.Colour('reset', True)]);
        reload_scripts(environment_dict);
        _templatescript.load_scripts(environment_dict);
        _plugins.load(environment_dict);
        _lldbcmd.execute_command('script', 'add', '-f ', 'lldbscript.lldbscript dbscript');
        environment_dict[INTERNAL_LOADED_NAME_CHECK] = True;


def lldbscript(debugger, command, result, internal_dict):
    response = _cmdmap.parse_command(command);