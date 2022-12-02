from os import walk
import os
import re

def sorted_nicely( l ):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

cur_dir = os.getcwd()
for (dirpath, dirnames, filenames) in walk(cur_dir):

    idx = 1
    for dir_name in sorted_nicely(dirnames):
        output_dir_name = dir_name.split(".")

        result = "{0}.".format(idx)
        if len(output_dir_name) == 2:
            result = "{0}{1}".format(result, output_dir_name[1])

        os.rename(dir_name, result)
        print("{0:20} => {1}".format(dir_name, result))
        idx += 1

    break