import _environment
import _colours


TYPE_KEY = 'type';
DATA_KEY = 'data';
COLOUR_KEY = 'colour';
STRING_KEY = 'string';
FORMATTER_KEY = 'formatter';
DISPLAY_KEY = 'display';
STATE_KEY = 'state';


def fmt(args):
    line = '';
    for item in args:
        item_type = item[TYPE_KEY];
        item_data = item[DATA_KEY];
        if item_type == COLOUR_KEY:
            colour_value = item_data[COLOUR_KEY];
            state_value = item_data[STATE_KEY];
            line += _colours.cmap(colour_value,state_value);
        elif item_type == STRING_KEY:
            formatter_value = item_data[FORMATTER_KEY];
            display_value = item_data[DISPLAY_KEY];
            line += formatter_value % display_value;
        else:
            line += '';
    
    print line;


def Colour(name, state):
    return {
        TYPE_KEY: COLOUR_KEY,
        DATA_KEY: {
            COLOUR_KEY: name,
            STATE_KEY: state
        }
    };


def String(formatter, value):
    return {
        TYPE_KEY: STRING_KEY,
        DATA_KEY: {
            FORMATTER_KEY: formatter,
            DISPLAY_KEY: value
        }
    };


def debuglog(args):
    if _environment.debuglog() == str(True):
        fmt(args);