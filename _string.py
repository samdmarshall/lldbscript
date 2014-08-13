import os
import shlex


def split_args(string):
	return shlex.split(string);


def last_word(string):
    return str(string).split(' ')[-1];


def get_file_name(path):
    name, extension = os.path.splitext(os.path.basename(path));
    return name;