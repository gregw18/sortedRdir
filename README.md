# Sorted Recursive Directory Lister

Given a filespec (i.e. \*.cpp) this Python script will check the current directory and all subdirectories for matching files and display them sorted by size or date, in one list. Use -s to sort by size and -d to sort by date.
This is a quick utility that I wrote to test my Python coding, that does something that I had previously wished existed in Windows. It sorts all the files from all the directories in one global list, rather than sorting the contents of each directory separately. 
eg. "python sortedRdir.py -d '*.py'" will show all the python files, sorted by last modified date. It's useful for things like finding the most recent copy of a given source file, when you haven't set up version control on a new machine yet and are using backup folders instead!
Appears to work under Linux and Windows. (Tested under Ubuntu 18.04 and Windows 7.)

## Getting Started

Copy script to convenient location on your system, go to directory that you want to search underneath, then use python to run the script.
eg:
python3 sortedRdir.py -s *.cpp

### Prerequisites

Python (tested with 3.6.)


## Authors

* **Greg Walker** - *Initial work* - (https://github.com/gregw18)


## License

MIT


