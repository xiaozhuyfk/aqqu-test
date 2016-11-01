"""
A few simple utitlity functions.

Copyright 2015, University of Freiburg.

Elmar Haussmann <haussmann@cs.uni-freiburg.de>

"""
from itertools import tee, izip
import codecs
import json

# Read a file
# filename is the path of the file, string type
# returns the content as a string
def readFile(filename, mode = "rt"):
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents


# Write 'contents' to the file
# 'filename' is the path of the file, string type
# 'contents' is of string type
# returns True if the content has been written successfully
def writeFile(filename, contents, mode = "wt"):
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

def codecsReadFile(filename, mode = "rt", encoding = 'utf-8'):
    # rt stands for "read text"
    f = contents = None
    try:
        f = codecs.open(filename, mode=mode, encoding=encoding)
        contents = f.read()
    finally:
        if (f != None): f.close()
    return contents

def codecsWriteFile(filename, contents, mode = "wt", encoding = 'utf-8'):
    f = None
    try:
        f = codecs.open(filename, mode=mode, encoding=encoding)
        f.write(contents)
    finally:
        if (f != None): f.close()
    return True

def codecsLoadJson(filename, mode = "rt", encoding = 'utf-8'):
    f = None
    d = None
    try:
        with codecs.open(filename, mode, encoding) as f:
            d = json.load(f)
    finally:
        if (f != None): f.close()
    return d

def codecsDumpJson(filename, contents, mode = "wt", encoding = 'utf-8'):
    f = None
    try:
        with codecs.open(filename, mode, encoding) as f:
            json.dump(contents, f)
    finally:
        if (f != None): f.close()
    return True


def edit_distance(s1, s2, compare_lower=True):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) < len(s2):
        return edit_distance(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def triplewise(iterable):
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return izip(a, b, c)


if __name__ == '__main__':
    print edit_distance('this is a house', 'this is not a house')
