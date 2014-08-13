#!/usr/bin/env python

import os

import _string
import _colours
import _print
import _lldbcmd
import _templatescript

CORE_SCRIPT_NAMES = ['_colours.py', '_string.py', '_print.py', '_lldbcmd.py', '_environment.py', '_templatescript.py'];

def build_script_path(script_name):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), script_name);


def reload_scripts(environment_dict):
    for script in CORE_SCRIPT_NAMES:
        if not _string.get_file_name(script) in environment_dict:
            script_path = build_script_path(script);
            _lldbcmd.execute_command('script', '', 'import', script_path);


def __lldb_init_module(debugger, environment_dict):
    if not 'dbscript' in environment_dict:
        _print.fmt([_print.Colour('blue', True), _print.Colour('bold', True), _print.String('%s', 'Loading lldbscript...'), _print.Colour('reset', True)]);
        reload_scripts(environment_dict);
        _templatescript.load_scripts(environment_dict);
        _lldbcmd.execute_command('script', 'add', '-f ', 'lldbscript.lldbscript dbscript');
        environment_dict['dbscript'] = True;

def lldbscript(debugger, command, result, internal_dict):
    print "testing!";