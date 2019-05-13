# Greg Walker, December, 2018.
# Program to get all files in current dir and all sub-dirs, then sort entire list by size or last modified date.
# Run -s to sort by size (default), -d to sort by date.
# Can also pass file pattern, to include only matching files. If running under linux, surround with
# single quote, to avoid wildcard expansion. i.e. "python sortedRdir.py -d '*.py'"

import fnmatch
import os
import time
import sys
from operator import itemgetter


def ParseArg(arg, sort_order, file_pattern):
    # See what is in given argument - sort order or file pattern.
    if arg[0] == "-":
        if arg[1].lower() == "d":
            sort_order = "d"    # Sort by date.
        elif arg[1].lower() == "s":
            sort_order = "s"
        else:
            print( "Unknown sort option provided: " + arg)
    else:
        file_pattern = arg
    #print("arg: ", arg, " Pattern: ", file_pattern, ", sort order: ", sort_order)

    return sort_order, file_pattern


def ParseArgs(argv):
    # See if was given any arguments.
    file_pattern = ""
    sort_order = "s"    # Default sort order to size.
    if len(argv) > 1:
        sort_order, file_pattern = ParseArg(argv[1], sort_order, file_pattern)
    if len(argv) > 2:
        sort_order, file_pattern = ParseArg(argv[2], sort_order, file_pattern)
    #print("Pattern: ", file_pattern, ", sort order: ", sort_order)

    return sort_order, file_pattern


def GetFileList(rootdir, file_pattern):
    # Get list of all files (not directories), including size and modified date.
    allfiles = []
    for root, dirs, files in os.walk(rootdir):
        #print("root: " + root)
        #print("len(dirs)", len(dirs))
        #print( os.path.join(root, name) for name in files)
        #print("len(files)", len(files))
        for name in files:
            #print("name: ", name)
            fullname = os.path.join(root, name)
            if len(file_pattern) == 0 or fnmatch.fnmatch(name, file_pattern):
                newdic = {"name": fullname, 
                        "size": os.path.getsize(fullname), 
                        "lastmod": os.path.getmtime(fullname) }
                allfiles.append(newdic)
    return allfiles


def GetSizeWidth(sortfiles):
    # Check max file size, ensure column is wide enough.
    size_col_width = 8
    if sortfiles[-1]["size"] > 999999999:
        size_col_width = 14
    elif sortfiles[-1]["size"] > 999999:
        size_col_width = 12
    return size_col_width


def PrintList(allFiles, sort_order):
    if len(allfiles) > 0:
        if sort_order == "s":
            sortfiles = sorted(allfiles, key=itemgetter("size"), reverse=False)
        elif sort_order == "d":
            sortfiles = sorted(allfiles, key=itemgetter("lastmod"), reverse=False)
        else:
            print( "Unexpected sort order requested: " + sort_order)    
        size_col_width = GetSizeWidth(sortfiles)

        for thisDic in sortfiles:
            time_str = time.strftime("%d/%m/%Y %I:%M%p",time.localtime(thisDic["lastmod"]))
            print(time_str.ljust(18), end="")
            print("{0:,}".format(thisDic["size"]).rjust(size_col_width), end=" ")
            print(thisDic["name"])


# See if was given any arguments.
sort_order, file_pattern = ParseArgs(sys.argv)

# Get list of all files (not directories), including size and modified date.
cwd = os.getcwd()
allfiles = GetFileList(cwd, file_pattern)

# Sort, then output.
PrintList(allfiles, sort_order)
