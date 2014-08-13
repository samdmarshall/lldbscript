import _environment


COLOUR_CODES = {
    'reset': (0, 0),
    'bold' : (22, 1),
    'italics': (23, 3),
    'underline': (24, 4),
    'inverse': (27, 7),
    'strike': (29, 9),
    'black': (40, 30),
    'red': (41, 31),
    'green': (42, 32),
    'yellow': (33, 43),
    'blue': (44, 34),
    'magenta': (45, 35),
    'cyan': (46, 36),
    'white': (47, 37),
    'default': (49, 39)
};


def term_supports_colour():
    return _environment.has_variable('TERM'); # this works for OS X, not sure about other platforms


# name - name of the colour from the COLOUR_CODES dict
# toggle - toggle state:
#           bold, italics, inverse, strike
#               True - enable
#               False - disable
#           black, red, green, yellow, blue, magenta, cyan, white, default
#               True - text colour
#               False - background colour
def cmap(name, toggle):
    code_list = ();
    if term_supports_colour() == True and name in COLOUR_CODES:
        code_list = COLOUR_CODES[name];
    if len(code_list) > 0:
        return '\x1b[' + str(code_list[int(toggle)]) + 'm';
    else:
        return '';