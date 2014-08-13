import os


def file_exists(path):
    return os.path.exists(path)


def make_dir(path):
    if file_exists(path) == False:
        os.mkdir(path)


def make_sym(original, path):
    if file_exists(path) == False:
        os.symlink(original, path)


def get_file_name(path):
    name, extension = os.path.splitext(os.path.basename(path));
    return name;