import _string
import _print
import _colours
import _plugins


def parse_command(command):
    argv = _string.split_args(command);
    argc = len(argv);
    index = 0;
    script_command = argv[index];
    plist = _plugins.get_plugin_list();
    valid_command = script_command in plist;
    if valid_command == True:
        _print.debuglog([_print.Colour('green',True), _print.String('%s', 'Found Command!'), _print.Colour('reset', True)]);
        command_instance = _plugins.get_plugin_instance(script_command)();
        command_map = command_instance.commands();
        index += 1;
        if argc > index:
            _print.debuglog([_print.Colour('green',True), _print.String('%s', 'Correct Number of Args...'), _print.Colour('reset', True)]);
            command_arg = argv[index];
            if command_arg in command_map.keys():
                _print.debuglog([_print.Colour('green',True), _print.String('%s', 'Valid Command Argument...'), _print.Colour('reset', True)]);
                command_func = command_map[command_arg];
                command_func();
            else:
                _print.debuglog([_print.Colour('red',True), _print.String('%s', 'Invalid Command Argument...'), _print.Colour('reset', True)]);
            
        else:
            _print.debuglog([_print.Colour('red',True), _print.String('%s', 'Incorrect Number of Args...'), _print.Colour('reset', True)]);
            command_instance.usage();
        
    else:
        _print.debuglog([_print.Colour('red',True), _print.String('%s', 'Invalid Command!'), _print.Colour('reset', True)]);