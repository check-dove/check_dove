#!/usr/bin/env python
"""---------------------------------------------------------------------------------"""
"""
                                    example in book
"""
"""---------------------------------------------------------------------------------"""
from urllib import urlretrieve


def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print(firstNonBlank(lines), )
    lines.reverse()
    print(firstNonBlank(lines), )


def download(url="http://www.bbaidu.com", process=firstLast):
    try:
        ret_val = urlretrieve(url)[0]
    except IOError:
        ret_val = None
    if ret_val:
        # do some processing
        process(ret_val)


"""---------------------------------------------------------------------------------"""

"""---------------------------------------------------------------------------------"""
"""
                            After   modification
"""
"""---------------------------------------------------------------------------------"""

if __name__ == '__main__':
    download()
