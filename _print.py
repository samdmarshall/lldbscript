import _environment
import _colours

def debuglog(args):
    if _environment.debuglog() == True:
        fmt(args);


def fmt(args):
    line = "";
    
    for item in args:
        item_type = item['type'];
        item_data = item['data'];
        
        if item_type == 'colour':
            colour_value = item_data['colour'];
            state_value = item_data['state'];
            line += _colours.cmap(colour_value,state_value);
        elif item_type == 'string':
            formatter_value = item_data['formatter'];
            display_value = item_data['display'];
            line += formatter_value % display_value;
        else:
            line += "";
    
    print line;


def Colour(name, state):
    return {
        'type': 'colour',
        'data': {
            'colour': name,
            'state': state
        }
    };


def String(formatter, value):
    return {
        'type': 'string',
        'data': {
            'formatter': formatter,
            'display': value
        }
    };