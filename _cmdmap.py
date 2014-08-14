import _string
import _print
import _colours
import _plugins


def parse_command(command):
    print_usage = len(command) == 0;
    if not print_usage:
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
                command_instance.print_usage();
            
        else:
            _print.debuglog([_print.Colour('red',True), _print.String('%s', 'Invalid Command!'), _print.Colour('reset', True)]);
            print_usage = True;
        
    if print_usage == True:
        known_commands = _plugins.get_plugin_list();
        print 'dbscript - Known Commands:';
        for command in known_commands:
            print '\t%s' % command;
        print '\nTo get usage information for a command enter: dbscript <command>';