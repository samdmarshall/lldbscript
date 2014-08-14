import os
import shlex
import string


def split_args(string):
	return shlex.split(string);


def last_word(string):
    return str(string).split(' ')[-1];


def split_by_char(string, char):
    return str(string).split(char);